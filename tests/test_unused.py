from code_analyzer.unused import find_unused_variables


def test_unused_local_variable_is_detected():
    """
    A variable that is assigned but never used should be reported.
    """
    source = (
        "def calculate():\n"
        "    unused = 10\n"
        "    result = 20\n"
        "    return result\n"
    )

    result = find_unused_variables(source)

    # 'unused' is assigned but never referenced.
    assert "unused" in result

    # 'result' is used by the return statement.
    assert "result" not in result


def test_used_variable_is_not_reported():
    """
    A variable that is assigned and later referenced should
    not be considered unused.
    """
    source = (
        "def calculate():\n"
        "    value = 10\n"
        "    result = value + 5\n"
        "    return result\n"
    )

    result = find_unused_variables(source)

    # Both variables are used.
    assert "value" not in result
    assert "result" not in result


def test_unused_function_parameter_is_detected():
    """
    A function parameter that is never referenced inside the
    function should be reported.
    """
    source = (
        "def calculate(value, unused):\n"
        "    return value\n"
    )

    result = find_unused_variables(source)

    assert "unused" in result
    assert "value" not in result


def test_used_function_parameter_is_not_reported():
    """
    A function parameter that is referenced should not be
    reported as unused.
    """
    source = (
        "def calculate(value):\n"
        "    return value + 10\n"
    )

    result = find_unused_variables(source)

    assert "value" not in result


def test_underscore_variable_is_ignored():
    """
    Variables beginning with an underscore are commonly used
    intentionally when the value is not required.

    The analyzer should therefore ignore them.
    """
    source = (
        "def process():\n"
        "    _unused = 10\n"
        "    return 5\n"
    )

    result = find_unused_variables(source)

    assert "_unused" not in result


def test_unused_loop_variable_is_detected():
    """
    A loop variable that is assigned but never referenced inside
    the loop should be reported.
    """
    source = (
        "def process(items):\n"
        "    for item in items:\n"
        "        print('processing')\n"
    )

    result = find_unused_variables(source)

    assert "item" in result


def test_used_loop_variable_is_not_reported():
    """
    A loop variable that is actually used inside the loop should
    not be reported.
    """
    source = (
        "def process(items):\n"
        "    for item in items:\n"
        "        print(item)\n"
    )

    result = find_unused_variables(source)

    assert "item" not in result


def test_multiple_unused_variables_are_detected():
    """
    Multiple unused variables should all be detected.
    """
    source = (
        "def process():\n"
        "    first = 1\n"
        "    second = 2\n"
        "    third = 3\n"
        "    return 10\n"
    )

    result = find_unused_variables(source)

    assert "first" in result
    assert "second" in result
    assert "third" in result