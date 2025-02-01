"""File to define River class."""

__author__ = "730761368"


from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())
        
    def check_ages(self):
        """This makes sure to removes the fish and bears that are too old."""
        # This part here it was hard for me to realize that i need to have 2 for loops
        fish_list: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                fish_list.append(fish)

        bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                bear_list.append(bear)
        self.fish = fish_list
        self.bears = bear_list

        return None

    def remove_fish(self, amount: int) -> None:
        """This makes sure to removes a certain amount of fish."""
        for i in range(amount):
            self.fish.pop(0)

    def bears_eating(self):
        """This makes sure to feed the bears in order until there arent enough fish left."""
        for i in self.bears:
            if len(self.fish) > 5:
                i.eat(num_fish=3)
                self.remove_fish(amount=3)
        return None

    def check_hunger(self):
        """This makes sure to remove the starving bears."""
        list_bear: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                list_bear.append(bear)
        self.bears = list_bear
        return None

    def repopulate_fish(self):
        """Repopulate the fish by (n//2)*4."""
        for i in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Repopulate the bears by n//2."""
        for i in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """View the river stats."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """This shows one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """This shows a week of activits on the river."""
        # I struggels a little bit here and found out to do the for loop
        for i in range(7):
            self.one_river_day()