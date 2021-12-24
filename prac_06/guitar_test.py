"""
CP1404 - Practical 6
Created on 24 December 2021 by Richard Reynard
"""

from CP1404.prac_06.guitar import Guitar


def main():
    """Test for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2013, 100)

    print(f"{guitar.name} get_age() - Expected 99. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 8. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()
