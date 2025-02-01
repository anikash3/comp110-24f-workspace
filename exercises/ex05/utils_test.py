__author__ = "730761368"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

def test_edge_only_evens() -> None: 
    assert(only_evens([1, 3, 7]) == []) # Edge Case

def test_use1_only_evens() -> None: 
    assert(only_evens([2, 4, 6]) == [2, 4, 6]) # Use Case 1
def test_use2_only_evens() -> None: 
    assert(only_evens([6, 8, 9]) == [6, 8]) # Use Case 2 

def test_edge_sub() -> None: 
    assert(sub([1, 2, 3, 4], -1, 6) == [1 ,2 ,3 ,4]) # Edge Case

def test_use1_sub() -> None: 
    assert(sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]) # Use Case 1

def test_use2_sub() -> None: 
    assert(sub([3, 4, 5], 2, 3) == [5]) # Use Case 2

def test_edge_add_at_index() -> None: 
    with pytest.raises(IndexError):# Edge Case
        add_at_index([], 1, 1)

def test_use1_add_at_index() -> None: 
    lst : list[int] = [1, 2, 3, 5]
    add_at_index(lst, 4, 3)
    assert(lst == [1, 2, 3, 4, 5]) # Use Case 1

def test_use2_add_at_index() -> None: 
    lst : list[int] = [1, 2] 
    add_at_index(lst, 3, 1)
    assert(lst == [1, 3, 2]) # Use Case 2