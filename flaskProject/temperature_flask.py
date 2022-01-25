"""
CP1404 - Practical
Pseudocode for temperature conversion refactored
Created on 24-01-22 by Richard Reynard
"""
from flask import Flask

MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""

app = Flask(__name__)


@app.route('/temperature')
def main():
    """Convert temperature."""
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "C":
        user_celsius = float(input("Celsius: "))
        fahrenheit = convert_celsius_to_fahrenheit(user_celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        user_fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_fahrenheit_to_celsius(user_fahrenheit)
        print("Result: {:.2f} F".format(celsius))
    print("Thank you.")


@app.route('/convert_celcius_to_fahrenheit')
def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route('/convert_fahrenheit_to_celcius')
def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


if __name__ == '__main__':
    app.run()
