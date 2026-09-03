from code_analyzer.duplicate import find_duplicate_code


def test_identical_function_bodies_are_detected():
    """
    Two functions with exactly the same body should be
    reported as duplicate code.
    """
    source = (
        "def first(value):\n"
        "    result = value + 1\n"
        "    return result\n"
        "\n"
        "def second(value):\n"
        "    result = value + 1\n"
        "    return result\n"
    )

    result = find_duplicate_code(source)

    assert ("first", "second") in result


def test_different_function_bodies_are_not_duplicates():
    """
    Functions with different logic should not be reported
    as duplicate code.
    """
    source = (
        "def first(value):\n"
        "    return value + 1\n"
        "\n"
        "def second(value):\n"
        "    return value + 2\n"
    )

    result = find_duplicate_code(source)

    assert result == []


def test_function_names_do_not_affect_duplicate_detection():
    """
    The function names themselves should not matter.
    Only the function body is compared.
    """
    source = (
        "def calculate(value):\n"
        "    total = value * 2\n"
        "    return total\n"
        "\n"
        "def process(value):\n"
        "    total = value * 2\n"
        "    return total\n"
    )

    result = find_duplicate_code(source)

    assert ("calculate", "process") in result


def test_whitespace_does_not_affect_duplicate_detection():
    """
    Different indentation/formatting should not prevent
    two logically identical AST bodies from being detected.
    """
    source = (
        "def first(value):\n"
        "    result = value + 1\n"
        "    return result\n"
        "\n"
        "def second(value):\n"
        "        result = value + 1\n"
        "        return result\n"
    )

    result = find_duplicate_code(source)

    assert ("first", "second") in result


def test_comments_do_not_affect_duplicate_detection():
    """
    Comments are not part of the AST structure used for
    comparison, so they should not prevent detection.
    """
    source = (
        "def first(value):\n"
        "    # calculate result\n"
        "    result = value + 1\n"
        "    return result\n"
        "\n"
        "def second(value):\n"
        "    # another comment\n"
        "    result = value + 1\n"
        "    return result\n"
    )

    result = find_duplicate_code(source)

    assert ("first", "second") in result


def test_function_is_not_reported_as_duplicate_of_itself():
    """
    A function must never be compared with itself.
    """
    source = (
        "def calculate(value):\n"
        "    return value + 1\n"
    )

    result = find_duplicate_code(source)

    assert result == []


def test_multiple_duplicate_functions_are_detected():
    """
    If several functions contain identical bodies, each
    duplicate pair should be identified.
    """
    source = (
        "def first(value):\n"
        "    return value + 1\n"
        "\n"
        "def second(value):\n"
        "    return value + 1\n"
        "\n"
        "def third(value):\n"
        "    return value + 1\n"
    )

    result = find_duplicate_code(source)

    assert ("first", "second") in result
    assert ("first", "third") in result
    assert ("second", "third") in result