'''This is a program that plans a Tea Party'''
__author__: str = "730761368"


def main_planner(guests:int) -> None:
    '''dispalsy the number of guests, teabags, treats and the total cost'''
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people = guests)))
    print("Treats: " + str(treats(people = guests)))
    print("Cost: $" + str(cost(tea_count = tea_bags(people = guests), treat_count = treats(people = guests))))

def tea_bags(people: int) -> int:
    '''calculates the number of teabags needed based on the number of people'''
    return people*2

#It took me some time to figure out that I needed to call the teabags funciton inside the treats
#I figured that this method helps abstract the code

def treats(people: int) -> int:
    '''calculates the number of treats needed based on the number of people'''
    return int(tea_bags(people = people)*1.5)


def cost(tea_count:int, treat_count:int) -> float:
    '''calulates the cost for tea and treats based on the quanity of each'''
    return tea_count*0.5 + treat_count*0.75


#In the beginning I didnt know why you could put this function at the top
#but later I figured out that the main planner function wouldn't have been defined so program wouldnt run


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

