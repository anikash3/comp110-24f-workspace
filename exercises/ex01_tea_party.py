__author__: str = "730761368"

def tea_bags(people: int) -> int:
    return people*2
#calculates the number of teabags needed based on the number of people

def treats(people: int) -> int:
    return int(tea_bags(people)*1.5)
#calculates the number of treats needed based on the number of people

def cost(tea_count:int, treat_count:int) -> float:
    return tea_count*0.5 + treat_count*0.75
#calulates the cost for tea and treats based on the quanity of each

def main_planner(guests:int) -> None:
    print("A Cost Tea Party for " + str(guests) + "!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

