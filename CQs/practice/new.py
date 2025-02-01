from __future__ import annotations

class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.value)

def sum_node_values(head: Node | None) -> int:
    if head.next == None:
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
        for i in range(len(head.value)):
            head.value[i] += 1
        return increment_node_values(head.next)

def print_nodes(head: Node | None) -> None:
    if head.next == None:
        print(head.value)
    else:
        print(head.value)
        return print_nodes(head.next)


node3 = Node([7, 8, 9], None)
node2 = Node([4, 5], node3)
node1 = Node([1, 2, 3], node2)

increment_node_values(node1)
print_nodes(node1)