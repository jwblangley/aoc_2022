from typing import NamedTuple


class Range(NamedTuple):
    """
    Represents a range of integers, inclusive at both ends
    """

    lower: int
    upper: int


def is_proper_subset_range(*rs: Range) -> bool:
    pass
