from solution import sum_sections

import pytest

@pytest.mark.parametrize("xs, exp", (
    (["1"], [1]),
    ([" 1 "], [1]),
    (["1","1"], [2]),
    (["1","1","1"], [3]),
    (["42"], [42]),
    (["1","2"], [3]),
    (["1","2","3"], [6]),
    (["10", "15", "25"], [50]),
    (["1",""], [1]),
    (["1","","1"], [1,1]),
    (["","1","1"], [2]),
    (["1","","2"], [1,2]),
    (["1","","2","3"], [1,5]),
    (["1","","2","3","","4","5","6"], [1,5,15]),
))
def test_sum_sections(xs, exp):
    # GIVEN
    """
    xs
    exp
    """

    # WHEN
    res = list(sum_sections(iter(xs)))

    # THEN
    assert res == exp
