import ast

"""
  Reference:
    - https://docs.python.org/3/library/ast.html
    - https://www.w3schools.com/python/ref_module_ast.asp
"""

def parse_source_code(source):
    """
    Validate and parse Python source code.

    This fucntion performs basic input validation before passing
    the source code to Python's Abstract Syntax Tree parser.

    Raises:
        TypeError: If source is not a string.
        ValueError: If source is empty or contains only whitespace.
        SyntaxError: If the Python source is syntactically invalid.
    """

    # Check the input is actually a string.
    # analyzer works with source-code text
    if not isinstance(source, str):
        raise TypeError("source must be a string")

    # Check whether the source contains any meaningful characters.
    # strip() removes spaces, tabs and newlines for this check.
    # Therefore, both "" and "   \n\t" are considered empty input.
    if not source.strip():
        raise ValueError("source cannot be empty")

    # Convert the Python source code into an Abstract Syntax Tree.
    #
    # ast.parse() performs Python syntax validation. If the source
    # contains invalid Python syntax, it automatically raises
    # SyntaxError.
    return ast.parse(source)