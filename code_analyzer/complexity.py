import ast


def calculate_complexity(source) :
    """
    Calculate cyclomatic complexity for each function.

    Complexity starts at 1 for every function. Each decision
    point increases the complexity by one.

    Decision points considered by this implementation are:

    - if statements
    - for loops
    - while loops
    - exception handlers
    - boolean AND operations
    - boolean OR operations
    - conditional expressions
    """

    # Convert the source code into an Abstract Syntax Tree.
    # The AST allows us to inspect the program without executing it.
    tree = ast.parse(source)

    # Store the calculated complexity for each function.
    complexities = {}

    # Visit every node in the syntax tree.
    for node in ast.walk(tree):

        # We are interested in normal and asynchronous functions.
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            # Every function starts with a base complexity of one.
            complexity = 1

            # Walk through the function's syntax tree.
            for child in ast.walk(node):

                # An if statement creates one additional path.
                if isinstance(child, ast.If):
                    complexity += 1

                # A for loop creates one additional path.
                elif isinstance(child, ast.For):
                    complexity += 1

                # A while loop creates one additional path.
                elif isinstance(child, ast.While):
                    complexity += 1

                # Each exception handler creates another path.
                elif isinstance(child, ast.ExceptHandler):
                    complexity += 1

                # Boolean operations are handled separately because
                # each additional AND/OR condition creates another
                # logical path.
                elif isinstance(child, ast.BoolOp):

                    # Count the number of boolean operators.
                    #
                    # For example:
                    #     a and b and c
                    #
                    # contains two AND operations.
                    complexity += len(child.values) - 1

                # A conditional expression such as:
                #     x = a if condition else b
                #
                # adds one decision point.
                elif isinstance(child, ast.IfExp):
                    complexity += 1

            # Store the final complexity using the function name.
            complexities[node.name] = complexity

    return complexities