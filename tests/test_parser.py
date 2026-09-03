import ast
import pytest
from code_analyzer.parser import parse_source_code


def test_valid_python_is_parsed():
    """
    This tests valid python source code can be parsed successfully
    It is a basic test. the inout is valid python and shold
    produce an Abstract syntax tree (AST), and python provide easy ast library.
    """

    # Parse a simple Python assignment.
    tree = parse_source_code("x = 10")

    # The returned object should be a Python AST Module.
    assert isinstance(tree, ast.Module)


def test_function_source_is_parsed():
    """
    Test that a Python function can be parsed correctly.

    This verifies that the parser is not only able to handle simple
    statements but can also process a function definition.
    Reference:
    - https://docs.python.org/3/library/ast.html
    - https://www.w3schools.com/python/ref_module_ast.asp
    """

    # Example Python source containing one function.
    source = (
        "def mutliply(a,b):\n"
        "    return a * b\n"
    )

    # parse source code.
    tree = parse_source_code(source)

    # the source must contain exactly one top-level statement
    assert len(tree.body) == 1

    # top-level statement should be a function definition
    assert isinstance(tree.body[0], ast.FunctionDef)

    # confirm that right function name was parsed
    assert tree.body[0].name == "mutliply"


def test_empty_source_is_rejected():
    """
    Test that an empty string is rejected

    ValueError should be returned instead of returning an empty AST.
    """

    # ValueError is expected when an empty source string is supplied.
    with pytest.raises(ValueError):
        parse_source_code("")


def test_whitespace_only_source_is_rejected():
    """
    Test source containing only whitespace is rejected.

    Spaces, tabs and newlines do not make meaningful Python
    source code for this analyzer.
    """

    # the input contains whitespace but no actual source code.
    with pytest.raises(ValueError):
        parse_source_code("   \n\t")


def test_non_string_source_is_rejected():
    """
    Test that non-string input is rejected.

    The parser expects Python source code in string form.
    Supplying another data type should result in a TypeError.
    """

    # None is deliberately used as an invalid input type.
    with pytest.raises(TypeError):
        parse_source_code(None)


def test_invalid_python_is_rejected():
    """
    Test that syntactically invalid Python is rejected.

    Python's AST parser should raise SyntaxError when the supplied
    source code cannot be parsed.
    """

    # This function definition has invalid Python syntax.
    with pytest.raises(SyntaxError):
        parse_source_code("def broken(:")


def test_single_line_with_trailing_newline_is_valid():
    """
    Tests boundary case involving a trailing newline.

    A normal source file can end with a newline. The parser should
    still treat the source as valid Python.
    """

    # 'pass' followed by a newline is valid Python source.
    tree = parse_source_code("pass\n")

    # The result should still be a valid AST.
    assert isinstance(tree, ast.Module)