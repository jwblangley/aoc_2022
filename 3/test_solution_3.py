import pytest

from solution_3 import get_intersection, get_priority


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


@pytest.mark.parametrize(
    ("char", "value"),
    [
        ("a", 1),
        ("b", 2),
        ("c", 3),
        ("d", 4),
        ("e", 5),
        ("f", 6),
        ("g", 7),
        ("h", 8),
        ("i", 9),
        ("j", 10),
        ("k", 11),
        ("l", 12),
        ("m", 13),
        ("n", 14),
        ("o", 15),
        ("p", 16),
        ("q", 17),
        ("r", 18),
        ("s", 19),
        ("t", 20),
        ("u", 21),
        ("v", 22),
        ("w", 23),
        ("x", 24),
        ("y", 25),
        ("z", 26),
        ("A", 27),
        ("B", 28),
        ("C", 29),
        ("D", 30),
        ("E", 31),
        ("F", 32),
        ("G", 33),
        ("H", 34),
        ("I", 35),
        ("J", 36),
        ("K", 37),
        ("L", 38),
        ("M", 39),
        ("N", 40),
        ("O", 41),
        ("P", 42),
        ("Q", 43),
        ("R", 44),
        ("S", 45),
        ("T", 46),
        ("U", 47),
        ("V", 48),
        ("W", 49),
        ("X", 50),
        ("Y", 51),
        ("Z", 52),
    ]
)
def test_get_priority(char, value):
    # GIVEN
    """
    char
    value
    """

    # WHEN
    res = get_priority(char)

    # THEN
    assert res == value
