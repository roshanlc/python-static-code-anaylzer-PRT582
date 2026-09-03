import ast

from code_analyzer.models import CodeMetrics


def calculate_metrics(source):
    """
    Calculate basic metrics for Python source code.

    Physical line metrics are calculated from the source text,
    while structural metrics such as functions, classes and
    imports are identified using Python's ast.
    """

    # Split the source into individual physical lines.
    #
    # splitlines() is used instead of split("\n") so that a
    # trailing newline does not create an unnecessary empty line.
    lines = source.splitlines()

    # Count lines that contain only whitespace.
    blank_lines = sum(
        1
        for line in lines
        if not line.strip()
    )

    # Count comment-only lines.
    #
    # A comment-only line is a line where the first non-whitespace
    # character is '#'.
    comment_lines = sum(
        1
        for line in lines
        if line.strip().startswith("#")
    )

    # Parse the Python source into an Abstract Syntax Tree.
    #
    # The AST lets us inspect the structure of the program
    # without executing the user's code.
    tree = ast.parse(source)

    # Count normal and asynchronous functions.
    #
    # ast.walk() recursively visits all nodes in the AST.
    functions = sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef)
        )
    )

    # Count class definitions.
    classes = sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef)
    )

    # Count both forms of import:
    #
    #     import os
    #
    # and:
    #
    #     from pathlib import Path
    imports = sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            (ast.Import, ast.ImportFrom)
        )
    )

    # Count non-blank source lines.
    #
    # This is the project's definition of the 'lines' metric.
    source_lines = sum(
        1
        for line in lines
        if line.strip()
    )

    # Return all calculated metrics as one structured object.
    return CodeMetrics(
        lines=source_lines,
        blank_lines=blank_lines,
        comment_lines=comment_lines,
        functions=functions,
        classes=classes,
        imports=imports,
    )