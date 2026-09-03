import ast
import re


def is_snake_case(name: str) -> bool:
    """
    Check whether a name follows snake_case naming.
    """
    return bool(re.fullmatch(r"[a-z_][a-z0-9_]*", name))


def is_pascal_case(name: str) -> bool:
    """
    Check whether a name follows PascalCase naming.
    """
    return bool(re.fullmatch(r"[A-Z][A-Za-z0-9]*", name))


def find_naming_violations(source: str) -> list[str]:
    """
    Find variable, function, parameter and class names
    that do not follow the required naming conventions.
    """

    tree = ast.parse(source)

    violations = []

    for node in ast.walk(tree):

        # Check function names.
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            if not is_snake_case(node.name):
                violations.append(node.name)

            # Check positional parameters.
            for argument in node.args.posonlyargs:
                if (
                    argument.arg not in ("self", "cls")
                    and not argument.arg.startswith("_")
                    and not is_snake_case(argument.arg)
                ):
                    violations.append(argument.arg)

            for argument in node.args.args:
                if (
                    argument.arg not in ("self", "cls")
                    and not argument.arg.startswith("_")
                    and not is_snake_case(argument.arg)
                ):
                    violations.append(argument.arg)

            # Check keyword-only parameters.
            for argument in node.args.kwonlyargs:
                if (
                    argument.arg not in ("self", "cls")
                    and not argument.arg.startswith("_")
                    and not is_snake_case(argument.arg)
                ):
                    violations.append(argument.arg)

            # Check *args.
            if node.args.vararg:
                name = node.args.vararg.arg

                if (
                    not name.startswith("_")
                    and not is_snake_case(name)
                ):
                    violations.append(name)

            # Check **kwargs.
            if node.args.kwarg:
                name = node.args.kwarg.arg

                if (
                    not name.startswith("_")
                    and not is_snake_case(name)
                ):
                    violations.append(name)

        # Check class names.
        elif isinstance(node, ast.ClassDef):

            if not is_pascal_case(node.name):
                violations.append(node.name)

        # Check variables.
        elif isinstance(node, ast.Name):

            if isinstance(node.ctx, ast.Store):
                if (
                    not node.id.startswith("_")
                    and not is_snake_case(node.id)
                ):
                    violations.append(node.id)

    return sorted(set(violations))