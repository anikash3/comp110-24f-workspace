"""File to define Bear class."""

__author__ = "730761368"


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor for class BEAR."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Changes the age and hunger when the day shifts."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Changes the hunger number depending how much the fish consumed."""
        self.hunger_score += num_fish