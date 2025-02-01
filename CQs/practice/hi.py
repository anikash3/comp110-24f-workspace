from __future__ import annotations
def fact(x: int) -> int:
    if x == 0:
        return (0)
    
    else:
        return x + fact(x-1)


class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next
    
    def __str__(self):
        return self.value

    
def sum_node_values(head: Node | None) -> int:
    if head == None:
        return 0
    else:
        sum = 0
        for i in head.value:
            sum += i

    return sum + sum_node_values(head.next)

def increment_node_values(head: Node | None) -> None:
    if head == None:
        return None
    
    else:
        for i in range(0,len(head.value):
            head.value[i] += 1
        increment_node_values(head.next)

def print_nodes(head: Node | None):
    if head = None:
        return None
    else:
        print(head)
        print_nodes(head.next)










    
