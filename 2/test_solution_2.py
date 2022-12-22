import pytest

from solution_2 import rpc_score


@pytest.mark.parametrize(
    ("moves", "exp"),
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


@pytest.mark.parametrize(
    ("moves", "exp"),
    (
        (["A X"], 3),
        (["A Y"], 4),
        (["A Z"], 8),
        (["B X"], 1),
        (["B Y"], 5),
        (["B Z"], 9),
        (["C X"], 2),
        (["C Y"], 6),
        (["C Z"], 7),
        (["A Y", "B X"], 5),
        (["B X", "B X"], 2),
        (["B X", "A Y"], 5),
        (["A Y", "B X", "C Z"], 12),
    ),
)
def test_rpc_score_play_for_outcome(moves, exp):
    # GIVEN
    """
    moves
    exp
    """

    # WHEN
    res = rpc_score(iter(moves), play_for_outcome=True)

    # THEN
    assert res == exp
