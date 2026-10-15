import pytest

from process import process


@pytest.mark.statement
@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([2], ["positivo", "par"], id="S1"),
    ],
)
def test_statement_coverage(values, expected):
    assert process(values) == expected

@pytest.mark.branch
@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([2, -1], ["positivo", "par"], id="D1"),
    ],
)
def test_branch_coverage(values, expected):
    assert process(values) == expected