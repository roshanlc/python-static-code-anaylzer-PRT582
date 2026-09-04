from code_analyzer.complexity import calculate_complexity
from code_analyzer.duplicate import find_duplicate_code
from code_analyzer.metrics import calculate_metrics
from code_analyzer.models import AnalysisResult
from code_analyzer.naming import find_naming_violations
from code_analyzer.unused import find_unused_variables


def analyze_source(source: str) -> AnalysisResult:
    """
    Run all static-code analyses on the supplied Python source.
    """

    # Calculate general code metrics.
    metrics = calculate_metrics(source)

    # Calculate cyclomatic-style complexity.
    complexity = calculate_complexity(source)

    # Find variables that are assigned but never used.
    unused_variables = find_unused_variables(source)

    # Find functions with duplicate bodies.
    duplicates = find_duplicate_code(source)

    # Find naming convention violations.
    naming_violations = find_naming_violations(source)

    # Combine all analysis results into one object.
    return AnalysisResult(
        metrics=metrics,
        complexity=complexity,
        unused_variables=unused_variables,
        duplicates=duplicates,
        naming_violations=naming_violations,
    )