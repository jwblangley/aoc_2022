from collections import Counter
from functools import reduce
import operator

from typing import TypeVar, Iterator, Generator

T = TypeVar("T")


def get_intersection(*ss: str) -> Counter[str]:
    # More efficient would be to stop counting as soon as we get one match for our specific use case
    return reduce(operator.and_, (Counter(s) for s in ss))


def get_priority(l: str) -> int:
    assert len(l) == 1, "get_priority is for a single char"
    assert "a" <= l <= "z" or "A" <= l <= "Z", "char is not an alphabetic character"

    if "a" <= l <= "z":
        return ord(l) - ord("a") + 1
    else:
        return ord(l) - ord("A") + 27


def counter_to_char(c: Counter[str]) -> str:
    assert len(c) == 1, "There should only be one intersecting key"
    return next(c.elements())


def split_line(line: str) -> tuple[str, str]:
    assert len(line) % 2 == 0, "Only even splits are allowed"
    return line[: len(line) // 2], line[len(line) // 2 :]


def batch(
    ts: Iterator[T], batch_size: int, assert_fits: bool = False
) -> Generator[list[T], None, None]:
    acc = list()
    for t in ts:
        acc.append(t)
        if len(acc) == batch_size:
            yield list(acc)
            acc.clear()
    if assert_fits and len(acc) > 0:
        raise ValueError(f"Iterable does not fit into batches of {batch_size}")
    if len(acc) > 0:
        yield acc


if __name__ == "__main__":
    with open("3/input.txt") as f:
        sum_priorities = sum(
            get_priority(counter_to_char(get_intersection(*split_line(line.strip()))))
            for line in f
        )
    print(f"1: Sum of priorities: {sum_priorities}")

    with open("3/input.txt") as f:
        sum_priorities = sum(
            get_priority(counter_to_char(get_intersection(*b)))
            for b in batch((line.strip() for line in f), 3, assert_fits=True)
        )
    print(f"2: Sum of priorities: {sum_priorities}")
