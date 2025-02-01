__author__ = "730761368"

def only_evens(lst: list[int]) -> list[int]:
    list = []
    for i in lst:
        if i % 2 == 0:
            list.append(i)
    return list


def sub(lst: list[int], start: int, end:int) -> list[int]:
    new = []

    if start < 0:
        start = 0
    if end > len(lst):
        end = len(lst)
    if len(lst) == 0 or start >= len(lst) or end <= 0:
        return []

    for i in range(start, end):
        new.append(lst[i])
    
    return new

def add_at_index(lst: list[int], what: int, index:int) -> None:
    if index < 0 or index > len(lst): 
        raise IndexError("Index is out of bounds for the input list")
    
    lst.append(what) 
    for item in range(len(lst) - 1, index, -1): 
        lst[item] = lst[item - 1]

    lst[index] = what







