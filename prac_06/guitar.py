"""
CP1404 - Practical 6
Created on 24 December 2021 by Richard Reynard
"""

CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    """Represent types of guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representing a particular guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Determine the age of a guitar based on the year of reference."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is considered vintage."""
        return self.get_age() >= VINTAGE_AGE
