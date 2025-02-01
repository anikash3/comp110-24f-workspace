"""What we did in class."""
from __future__ import annotations
__author__ = "730761368"


class Node:
    """This is the Node class."""
    value: int 
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """This is the constructior."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represents the linked list as a string value."""
        rest: str = ""
        if self.next is None:  # Base case when the next node is None
            rest = "None"
        else: 
            rest = str(self.next)  # Recursive case that goes toward base case
        return f"{self.value} -> {rest}"


def last(head: Node) -> int: 
    """This finds the last value of the linked list."""
    if head.next is None: 
        return head.value
    else: 
        rest: int = last(head.next)
        return rest


def value_at(head: Node | None, index: int) -> int:
    """This finds the value at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """This finds the max."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    max_item = max(head.next)
    if head.value > max_item:
        return head.value 
    else:
        return max_item


def linkify(items: list[int]) -> Node | None:
    """Return values in the same order as the input list based on the given secondary arguement."""
    if items == []:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Rreturns each value in the original list is multiplied by the scaling factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))