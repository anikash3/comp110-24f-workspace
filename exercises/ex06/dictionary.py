__author__ = "730761368"

def invert(orig: dict[str, str]) -> dict[str, str]:
    new: dict[str, str] = {}
    num: int = 0

    for i in orig: 
        for j in orig: 
            if orig[i] == orig[j]:  # Checks if two different keys have the same value
                num += 1  # Increments counter when duplicate value is found
        if num > 1: 
            raise KeyError("same keys are repeated")
        else:
            num = 0  # Resets counter for the next iteration
    
    for i in orig:
        new[orig[i]] = i

    return new 


def favorite_color(dict: dict[str, str]) -> str:
    max: int = 0
    color: str = ""
    for i in dict:
        num: int = 0
        for j in dict:
            if dict[i] == dict[j]:  # Counts how many times the current color appears in 'dict'
                num += 1

        if num > max:  # Updates 'max' if the current color count is the highest so far
            max = num
            color = dict[i]  # Sets 'color' to the most frequently occurring color
    
    return color


def count(lst: list[str]) -> dict[str, int]:
    final: dict[str, int] = {}
    
    for i in lst:
        if i in final:
            final[i] += 1  # Increments count if the string is already in the dictionary
        else:
            final[i] = 1  # Initializes count at 1 for new strings
    
    return final  # Returns the dictionary containing counts of each string


def alphabetizer(lst: list[str]) -> dict[str, list[str]]:
    final: dict[str, list[str]] = {}
    for i in lst:
        first = i[0].lower()  # Gets the first letter of the string in lowercase
        if first not in final:  # Checks if this letter has been used as a key in 'final'
            final[first] = []  # Initializes an empty list for new letters
        final[first].append(i) 

    return final


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    if day in log:
        if student not in log[day]:
            log[day].append(student)
    else:
        log[day] = [student]