from code_analyzer.metrics import calculate_metrics


def test_empty_program_has_zero_metrics():
    pass


def test_blank_lines_are_counted():
   pass


def test_comment_lines_are_counted():
   pass


def test_functions_are_counted():
    pass
    result = calculate_metrics(source)

    # Two function definitions are present.
    assert result.functions == 2


def test_classes_are_counted():
   pass


def test_imports_are_counted():
    pass


def test_trailing_newline_is_not_an_extra_source_line():
    pass

def test_async_functions_are_counted():
    pass