from code_analyzer.complexity import calculate_complexity


def test_simple_function_has_complexity_one():
    """
    A function with no decision points should have a
    cyclomatic complexity of 1.

    The base complexity of every function is one.
    """
    source = (
        "def greet(name):\n"
        "    return name\n"
    )

    result = calculate_complexity(source)

    assert result["greet"] == 1


def test_if_statement_adds_one_to_complexity():
    """
    An if statement represents one decision point.

    Therefore, a simple function containing one if statement
    should have complexity 2.
    """
    source = (
        "def check(value):\n"
        "    if value > 10:\n"
        "        return True\n"
        "    return False\n"
    )

    result = calculate_complexity(source)

    assert result["check"] == 2


def test_for_loop_adds_one_to_complexity():
    """
    A for loop represents one decision point.

    The function therefore has a complexity of 2.
    """
    source = (
        "def process(items):\n"
        "    for item in items:\n"
        "        print(item)\n"
    )

    result = calculate_complexity(source)

    assert result["process"] == 2


def test_while_loop_adds_one_to_complexity():
    """
    A while loop represents one decision point.

    The expected complexity is therefore 2.
    """
    source = (
        "def count_down(value):\n"
        "    while value > 0:\n"
        "        value -= 1\n"
    )

    result = calculate_complexity(source)

    assert result["count_down"] == 2


def test_except_handler_adds_one_to_complexity():
    """
    An exception handler represents a decision point.

    A function containing one except block should therefore
    have complexity 2.
    """
    source = (
        "def read_value(value):\n"
        "    try:\n"
        "        return int(value)\n"
        "    except ValueError:\n"
        "        return 0\n"
    )

    result = calculate_complexity(source)

    assert result["read_value"] == 2


def test_and_operator_adds_one_to_complexity():
    """
    A boolean AND condition introduces an additional logical
    decision point.

    Therefore, the complexity should increase from 1 to 2.
    """
    source = (
        "def check(value):\n"
        "    if value > 10 and value < 20:\n"
        "        return True\n"
        "    return False\n"
    )

    result = calculate_complexity(source)

    # One point comes from the if and one from the AND.
    assert result["check"] == 3


def test_or_operator_adds_one_to_complexity():
    """
    A boolean OR condition introduces an additional logical
    decision point.
    """
    source = (
        "def check(value):\n"
        "    if value == 1 or value == 2:\n"
        "        return True\n"
        "    return False\n"
    )

    result = calculate_complexity(source)

    # One point comes from the if and one from the OR.
    assert result["check"] == 3


def test_nested_decisions_are_counted():
    """
    Multiple nested decision points should all contribute
    to the function's complexity.
    """
    source = (
        "def check(a, b):\n"
        "    if a > 0:\n"
        "        if b > 0:\n"
        "            return True\n"
        "    return False\n"
    )

    result = calculate_complexity(source)

    # Base 1 + first if + second if = 3.
    assert result["check"] == 3


def test_conditional_expression_adds_one():
    """
    A conditional expression is also a decision point.

    Example:
        result = "yes" if value else "no"
    """
    source = (
        "def choose(value):\n"
        "    result = 'yes' if value else 'no'\n"
        "    return result\n"
    )

    result = calculate_complexity(source)

    assert result["choose"] == 2