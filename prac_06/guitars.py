"""
CP1404 - Practical 6
Created on 24 December 2021 by Richard Reynard
"""

from CP1404.prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar_add = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar_add)
        print(f"{guitar_add} added.")
        guitar_name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("I have these guitars:")
    for i, guitar in enumerate(guitars):
        print(f"{guitar.name:20}, Price: {guitar.cost:6} from year {guitar.year} ")


main()
