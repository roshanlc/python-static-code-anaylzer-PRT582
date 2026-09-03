from dataclasses import dataclass


@dataclass(frozen=True)
class CodeMetrics:
    """
    Stores the code metrics calculated by the analyzer.
    """

    # Number of non-blank source lines.
    lines: int

    # Number of blank lines.
    blank_lines: int

    # Number of comment-only lines.
    comment_lines: int

    # Number of function definitions.
    functions: int

    # Number of class definitions.
    classes: int

    # Number of import statements.
    imports: int