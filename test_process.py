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

@pytest.mark.path
@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param(
            [2, 2],
            ["positivo", "par", "positivo", "par"],
            id="P01-R1-R1",
        ),
        pytest.param(
            [2, 1],
            ["positivo", "par", "positivo"],
            id="P02-R1-R2",
        ),
        pytest.param(
            [2, 0],
            ["positivo", "par", "par"],
            id="P03-R1-R3",
        ),
        pytest.param(
            [2, -1],
            ["positivo", "par"],
            id="P04-R1-R4",
        ),
        pytest.param(
            [1, 2],
            ["positivo", "positivo", "par"],
            id="P05-R2-R1",
        ),
        pytest.param(
            [1, 1],
            ["positivo", "positivo"],
            id="P06-R2-R2",
        ),
        pytest.param(
            [1, 0],
            ["positivo", "par"],
            id="P07-R2-R3",
        ),
        pytest.param(
            [1, -1],
            ["positivo"],
            id="P08-R2-R4",
        ),
        pytest.param(
            [0, 2],
            ["par", "positivo", "par"],
            id="P09-R3-R1",
        ),
        pytest.param(
            [0, 1],
            ["par", "positivo"],
            id="P10-R3-R2",
        ),
        pytest.param(
            [0, 0],
            ["par", "par"],
            id="P11-R3-R3",
        ),
        pytest.param(
            [0, -1],
            ["par"],
            id="P12-R3-R4",
        ),
        pytest.param(
            [-1, 2],
            ["positivo", "par"],
            id="P13-R4-R1",
        ),
        pytest.param(
            [-1, 1],
            ["positivo"],
            id="P14-R4-R2",
        ),
        pytest.param(
            [-1, 0],
            ["par"],
            id="P15-R4-R3",
        ),
        pytest.param(
            [-1, -1],
            [],
            id="P16-R4-R4",
        ),
    ],
)
def test_path_coverage(values, expected):
    assert process(values) == expected