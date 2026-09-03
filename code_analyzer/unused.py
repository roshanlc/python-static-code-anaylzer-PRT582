import ast


class VariableUsageVisitor(ast.NodeVisitor):
    """
    Visit a function and record variables that are assigned
    and variables that are subsequently used.
    """

    def __init__(self):
        # Store names that are assigned values.
        self.assigned = set()

        # Store names that are actually referenced.
        self.used = set()

    def visit_Name(self, node):
        """
        Process variable names in the AST.

        A Name node can represent either an assignment or a
        reference depending on its context.
        """

        # Store variables when they are assigned.
        if isinstance(node.ctx, ast.Store):
            self.assigned.add(node.id)

        # Store variables when they are read/referenced.
        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)

        # Continue visiting child nodes.
        self.generic_visit(node)


def find_unused_variables(source: str) -> list[str]:
    """
    Find variables that are assigned but never used.

    The analysis includes:
    - local variables
    - function parameters
    - loop variables

    Names beginning with '_' are ignored because they commonly
    represent intentionally unused values.
    """

    # Parse the source code without executing it.
    tree = ast.parse(source)

    unused = set()

    # Analyse every function independently.
    for function in (
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ):
        visitor = VariableUsageVisitor()

        # Check function parameters.
        for argument in function.args.posonlyargs:
            visitor.assigned.add(argument.arg)

        for argument in function.args.args:
            visitor.assigned.add(argument.arg)

        for argument in function.args.kwonlyargs:
            visitor.assigned.add(argument.arg)

        # Check *args.
        if function.args.vararg:
            visitor.assigned.add(function.args.vararg.arg)

        # Check **kwargs.
        if function.args.kwarg:
            visitor.assigned.add(function.args.kwarg.arg)

        # Visit the function body to find assignments and uses.
        for statement in function.body:
            visitor.visit(statement)

        # A variable is unused when it was assigned but never
        # referenced.
        for name in visitor.assigned - visitor.used:

            # Ignore intentionally unused/private-style names.
            if not name.startswith("_"):
                unused.add(name)

    return sorted(unused)