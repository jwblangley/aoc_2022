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


if __name__ == "__main__":
    calories_per_elf = sorted(sum_sections(open("1/input.txt")))
    print(f"Largest number of calories per elf: {calories_per_elf[-1]}")

    print(f"Total number of calories for top three elves: {sum(calories_per_elf[-3:])}")
