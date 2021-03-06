from typing import Generator, Iterable, List


def transpose(m: List[str]) -> List[str]:
    return [" ".join(row.split()[i] for row in m) for i in range(len(m))]


def flatten(items: Iterable) -> Generator:
    for e in items:
        if isinstance(e, Iterable) and not isinstance(e, (str, bytes)):
            yield from flatten(e)
        else:
            yield e


def sum_last_column(path: str) -> int:
    with open(path) as f:
        return sum(int(line.split()[-1]) for line in f)


def qsort(xs: List[int]) -> List[int]:
    lt_x = [y for y in xs[1:] if y < xs[0]]
    gt_x = [y for y in xs[1:] if y >= xs[0]]
    return qsort(lt_x) + [xs[0]] + qsort(gt_x) if xs else []


def subsets(xs: list) -> List[list]:
    return (
        subsets(xs[1:]) + [x + [xs[0]] for x in subsets(xs[1:])]
        if xs
        else [[]]
    )
