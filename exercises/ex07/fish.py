"""File to define Fish class."""

__author__ = "730761368"


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Constructor for Class FISH."""
        self.age = 0
        return None

    def one_day(self):
        """Changes/increases the age of the fish when day shifts."""
        self.age += 1
        return None