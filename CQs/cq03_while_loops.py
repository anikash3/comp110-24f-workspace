"""A while loop challenge in COMP 110."""

__author__ = "730761368"

def num_instances(phrase : str, search_char : str) -> int: 
    count : int = 0
    index = 0 # Rather than putting this variable here, I put it outside of the function which caused an unbounded error. Now the function can actually access the value of index. 
    while (index < len(phrase)):
        if(phrase[index] == search_char): 
            count += 1
            index += 1
            return count