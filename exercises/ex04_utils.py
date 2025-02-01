__author__: str = "730761368"

def all(lst: list[int], number: int) -> bool:
    if len(lst) == 0:
        return False
    for i in lst:
        if i != number:
            return False

    return True
    

def max(lst: list[int]) -> int:
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")

    
    max:int = lst[0]
    for i in lst:
        if i > max:
            max = i

    return max
    

def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False
    
        return True
    else:
        return False

def extend(lst1: list[int], lst2: list[int]) -> None:
    for i in lst2:
        lst1.append(i)

    print(lst1)

