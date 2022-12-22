import pytest

from solution_3 import get_intersection


@pytest.mark.parametrize(
    ("strs", "exp"),
    [
        (["a", "b"], ""),
        (["aa", "bc"], ""),
        (["aa", "ba"], "a"),
        (["aa", "ab"], "a"),
        (["ab", "ba"], "ab"),
        (["abc", "cba"], "abc"),
        (["abbc", "abcc"], "abc"),
        (["abbc", "abbb"], "abb"),
        (["vJrwpWtwJgWr", "hcsFMMfFFhFp"], "p"),
        (["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"], "LL"),
    ]
)
def test_get_intersect(strs, exp):
    # GIVEN
    a, b = strs
    """
    exp
    """

    # WHEN
    res = get_intersection(a, b)

    # THEN
    assert sorted(res.elements()) == sorted(exp)
