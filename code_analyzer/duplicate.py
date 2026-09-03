import ast
from itertools import combinations


def find_duplicate_code(source):
    """
    Find functions that contain identical code structures.

    The function bodies are converted into AST representations
    and compared. Function names themselves are ignored.
    """

    # Parse the Python source into an Abstract Syntax Tree.
    tree = ast.parse(source)

    # Store all functions found in the source file.
    functions = [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]

    duplicates = []

    # Compare every possible pair of functions.
    for first, second in combinations(functions, 2):

        # Convert each function body into a comparable AST string.
        first_body = ast.dump(
            ast.Module(body=first.body, type_ignores=[]),
            include_attributes=False,
        )

        second_body = ast.dump(
            ast.Module(body=second.body, type_ignores=[]),
            include_attributes=False,
        )

        # If the AST structures are identical, the functions
        # contain duplicate code.
        if first_body == second_body:
            duplicates.append((first.name, second.name))

    return duplicates
