import pytest

from solution_4 import Range, is_proper_subset_range, overlaps


@pytest.mark.parametrize(
    ("ranges", "exp"),
    [
        ([(1, 10), (5, 7)], True),
        ([(5, 7), (5, 7)], True),
        ([(5, 6), (5, 7)], True),
        ([(5, 7), (5, 6)], True),
        ([(4, 7), (5, 7)], True),
        ([(5, 7), (4, 7)], True),
        ([(5, 6), (6, 7)], False),
        ([(1, 5), (2, 10)], False),
        ([(1, 5), (2, 6)], False),
        ([(2, 6), (1, 5)], False),
    ],
)
def test_is_proper_subset_range(ranges, exp):
    # GIVEN
    """
    ranges
    exp
    """

    # WHEN
    res = is_proper_subset_range(*(Range(*r) for r in ranges))

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    ("ranges", "exp"),
    [
        ([(1, 5), (4, 10)], True),
        ([(1, 5), (5, 10)], True),
        ([(1, 5), (6, 10)], False),
        ([(4, 10), (1, 5)], True),
        ([(5, 10), (1, 5)], True),
        ([(6, 10), (1, 5)], False),
        ([(1, 10), (3, 6)], True),
        ([(3, 6), (1, 10)], True),
        ([(3, 6), (3, 6)], True),
    ],
)
def test_overlaps(ranges, exp):
    # GIVEN
    """
    ranges
    exp
    """

    # WHEN
    res = overlaps(*(Range(*r) for r in ranges))

    # THEN
    assert res == exp
