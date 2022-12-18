import pytest

from solution_2 import rpc_score


@pytest.mark.parametrize(
    "moves, exp",
    (
        (["A X"], 4),
        (["A Y"], 8),
        (["A Z"], 3),
        (["B X"], 1),
        (["B Y"], 5),
        (["B Z"], 9),
        (["C X"], 7),
        (["C Y"], 2),
        (["C Z"], 6),
        (["A Y"], 8),
        (["B X"], 1),
        (["C Z"], 6),
        (["A Y", "B X"], 9),
        (["B X", "B X"], 2),
        (["B X", "A Y"], 9),
        (["A Y", "B X", "C Z"], 15),
    ),
)
def test_rpc_score(moves, exp):
    # GIVEN
    """
    moves
    exp
    """

    # WHEN
    res = rpc_score(iter(moves))

    # THEN
    assert res == exp
