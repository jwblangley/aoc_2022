from collections import Counter

def get_intersection(a: str, b: str) -> Counter[str]:
    # More efficient would be to stop counting as soon as we get one match
    return Counter(a) & Counter(b)

def get_priority(l: str) -> int:
    pass
