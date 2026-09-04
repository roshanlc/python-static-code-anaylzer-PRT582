from code_analyzer.analyzer import analyze_source
from code_analyzer.models import AnalysisResult


def test_analyzer_returns_complete_result():
    """
    The main analyzer should return one object containing
    the results from all five analysis features.
    """

    source = (
        "import os\n"
        "\n"
        "class userAccount:\n"
        "    def calculateTotal(badParameter):\n"
        "        unused_value = 10\n"
        "        return badParameter\n"
        "\n"
        "def another_function(value):\n"
        "    return value + 1\n"
    )

    result = analyze_source(source)

    assert isinstance(result, AnalysisResult)

    assert result.metrics.imports == 1
    assert result.metrics.classes == 1
    assert result.metrics.functions == 2

    assert "unused_value" in result.unused_variables

    assert "userAccount" in result.naming_violations
    assert "calculateTotal" in result.naming_violations
    assert "badParameter" in result.naming_violations


def test_analyzer_detects_complexity():
    """
    The integrated analyzer should include complexity results.
    """

    source = (
        "def check(value):\n"
        "    if value > 10:\n"
        "        return True\n"
        "    return False\n"
    )

    result = analyze_source(source)

    assert result.complexity["check"] == 2


def test_analyzer_detects_duplicate_functions():
    """
    The integrated analyzer should include duplicate-code results.
    """

    source = (
        "def first(value):\n"
        "    return value + 1\n"
        "\n"
        "def second(value):\n"
        "    return value + 1\n"
    )

    result = analyze_source(source)

    assert ("first", "second") in result.duplicates


def test_clean_source_produces_no_violations():
    """
    A simple clean program should produce no unused variables,
    duplicate functions or naming violations.
    """

    source = (
        "def calculate_total(value):\n"
        "    result = value + 10\n"
        "    return result\n"
    )

    result = analyze_source(source)

    assert result.unused_variables == []
    assert result.duplicates == []
    assert result.naming_violations == []