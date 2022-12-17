from typing import Iterator, Generator

def sum_sections(xs: Iterator[str]) -> Generator[int, None, None]:
    total = 0
    for x in xs:
        if x.strip() == "":
            if total != 0:
                yield total
                total = 0
            continue
        total += int(x)
    if total != 0:
        yield total
