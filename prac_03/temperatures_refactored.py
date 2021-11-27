"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion refactored
Created on 27-11-21 by Richard Reynard
"""

MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    """Convert temperature."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            user_celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(user_celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            user_fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(user_fahrenheit)
            print("Result: {:.2f} F".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
