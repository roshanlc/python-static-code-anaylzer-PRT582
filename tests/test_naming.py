from code_analyzer.naming import find_naming_violations


def test_valid_variable_name_is_not_reported():
    source = (
        "def calculate():\n"
        "    total_amount = 100\n"
        "    return total_amount\n"
    )

    result = find_naming_violations(source)

    assert result == []


def test_invalid_variable_name_is_reported():
    source = (
        "def calculate():\n"
        "    totalAmount = 100\n"
        "    return totalAmount\n"
    )

    result = find_naming_violations(source)

    assert "totalAmount" in result


def test_valid_function_name_is_not_reported():
    source = (
        "def calculate_total():\n"
        "    return 10\n"
    )

    result = find_naming_violations(source)

    assert result == []


def test_invalid_function_name_is_reported():
    source = (
        "def calculateTotal():\n"
        "    return 10\n"
    )

    result = find_naming_violations(source)

    assert "calculateTotal" in result


def test_valid_class_name_is_not_reported():
    source = (
        "class UserAccount:\n"
        "    pass\n"
    )

    result = find_naming_violations(source)

    assert result == []


def test_invalid_class_name_is_reported():
    source = (
        "class userAccount:\n"
        "    pass\n"
    )

    result = find_naming_violations(source)

    assert "userAccount" in result


def test_invalid_parameter_name_is_reported():
    source = (
        "def calculate(totalAmount):\n"
        "    return totalAmount\n"
    )

    result = find_naming_violations(source)

    assert "totalAmount" in result


def test_valid_parameter_name_is_not_reported():
    source = (
        "def calculate(total_amount):\n"
        "    return total_amount\n"
    )

    result = find_naming_violations(source)

    assert result == []


def test_self_and_cls_are_ignored():
    source = (
        "class User:\n"
        "    def update(self, cls):\n"
        "        return 10\n"
    )

    result = find_naming_violations(source)

    assert result == []


def test_underscore_names_are_ignored():
    source = (
        "def process():\n"
        "    _temporaryValue = 10\n"
        "    return _temporaryValue\n"
    )

    result = find_naming_violations(source)

    assert "_temporaryValue" not in result