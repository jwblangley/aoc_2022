from typing import NamedTuple


class Range(NamedTuple):
    """
    Represents a range of integers, inclusive at both ends
    """

    lower: int
    upper: int


def is_proper_subset_range(*rs: Range) -> bool:
    minimin = min(*rs, key=(lambda r: r.lower)).lower
    maximax = max(*rs, key=(lambda r: r.upper)).upper

    # Need to check equality since there may be shared boundaries
    return any(r == Range(minimin, maximax) for r in rs)
