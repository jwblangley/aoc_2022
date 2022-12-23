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


def overlaps(*rs: Range) -> bool:
    for r in rs:
        other_rs = list(rs)
        other_rs.remove(r)
        if any(other_r.lower <= r.upper <= other_r.upper for other_r in other_rs):
            return True
    return False


def line_to_ranges(line: str) -> tuple[Range, Range]:
    match [r.split("-") for r in line.strip().split(",")]:
        case [[ll, lu], [rl, ru]]:
            return Range(int(ll), int(lu)), Range(int(rl), int(ru))
        case _:
            raise ValueError(f'Could not parse line: "{line}"')


if __name__ == "__main__":
    with open("4/input.txt") as f:
        num_total_overlaps = sum(
            1 for line in f if is_proper_subset_range(*line_to_ranges(line))
        )
    print(f"Num total overlaps: {num_total_overlaps}")
