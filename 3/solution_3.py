from collections import Counter


def get_intersection(a: str, b: str) -> Counter[str]:
    # More efficient would be to stop counting as soon as we get one match
    return Counter(a) & Counter(b)


def get_priority(l: str) -> int:
    assert len(l) == 1, "get_priority is for a single char"
    assert "a" <= l <= "z" or "A" <= l <= "Z", "char is not an alphabetic character"

    if "a" <= l <= "z":
        return ord(l) - ord("a") + 1
    else:
        return ord(l) - ord("A") + 27
