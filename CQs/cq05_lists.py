"""Mutating functions."""

__author__ = "730761368"

def manual_append(lst: list[int], value: int) -> None:
    lst.append(value)


def double(lst: list[int]) -> None:
    i: int = 0
    while i < len(lst):
        lst[i] *= 2
        i += 1



list_1 : list[int] = [1,2,3]
list_2 : list[int] = list_1

double(list_2)
print(list_1)
print(list_2)