__author__ = '730761368'

a = [5,5,1,2,3,4,5,5,5]
def find_and_remove_max(lst: list[int]) -> int:
    if len(lst) != 0:
        max = lst[0]
        for i in lst:
            if i > max:
                max = i
        
        index = 0
        while index < len(lst):
            if lst[index] == max:
                lst.pop(max)
            else:
                index += 1
        return max
    else:
        return -1

print(find_and_remove_max(a))

print(a)


