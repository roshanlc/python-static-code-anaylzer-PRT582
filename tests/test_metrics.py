from code_analyzer.metrics import calculate_metrics


def test_empty_program_has_zero_metrics():
    """
    Test  basic case containing one executable statement.

    This verifies that a simple Python program is analysed correctly
    and that metrics which are not present return zero.
    """
    result = calculate_metrics("pass")

    # 'pass' is one non-blank source line.
    assert result.lines == 1

    # There are no blank lines.
    assert result.blank_lines == 0

    # There are no comment-only lines.
    assert result.comment_lines == 0

    # There are no functions.
    assert result.functions == 0

    # There are no classes.
    assert result.classes == 0

    # There are no imports.
    assert result.imports == 0


def test_blank_lines_are_counted():
    """
    Test that blank physical lines are counted correctly.

    Two blank lines are placed between two statements.
    """
    source = "x = 1\n\n\ny = 2"

    result = calculate_metrics(source)

    # Only x = 1 and y = 2 are non-blank lines.
    assert result.lines == 2

    # Two blank lines should be detected.
    assert result.blank_lines == 2


def test_comment_lines_are_counted():
    """
    Test that comment-only lines are identified correctly.

    The source contains two comments and one executable statement.
    """
    source = "# first comment\nx = 1\n# second comment"

    result = calculate_metrics(source)

    # All three physical lines are non-blank.
    assert result.lines == 3

    # Two of the lines contain comments.
    assert result.comment_lines == 2


def test_functions_are_counted():
    """
    Test that function definitions are counted.

    The source contains two functions, so the expected count is two.
    """
    source = (
        "def first():\n"
        "    pass\n"
        "\n"
        "def second():\n"
        "    pass\n"
    )

    result = calculate_metrics(source)

    # Two function definitions are present.
    assert result.functions == 2


def test_classes_are_counted():
    """
    Test that class definitions are counted.

    The source contains two classes.
    """
    source = (
        "class User:\n"
        "    pass\n"
        "\n"
        "class Admin:\n"
        "    pass\n"
    )

    result = calculate_metrics(source)

    # Two class definitions are present.
    assert result.classes == 2


def test_imports_are_counted():
    """
    Test that Python import statements are counted.

    Both 'import' and 'from ... import ...' forms are included.
    """
    source = (
        "import os\n"
        "import sys\n"
        "from pathlib import Path\n"
    )

    result = calculate_metrics(source)

    # Three import statements are present.
    assert result.imports == 3


def test_trailing_newline_is_not_an_extra_source_line():
    """
    Test the boundary condition where the source ends with a newline.

    A trailing newline should not create an additional source line.
    """
    result = calculate_metrics("pass\n")

    # The source contains only one actual source line.
    assert result.lines == 1


def test_async_functions_are_counted():
    """
    Test that asynchronous functions are included in the
    function count.
    """
    source = (
        "async def fetch():\n"
        "    pass\n"
    )

    result = calculate_metrics(source)

    # The async function should count as one function.
    assert result.functions == 1