"""
CP1404 Practical 5
Hexadecimal Colour Codes
Created on 16-12-2021 by Richard Reynard
"""

COLOUR_CODES = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue" : "#f0f8ff",
                "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "ffbf00", "Amethyst": "#9966cc",
                "AntiqueWhite": "#faebd7", "Bleu de France": "#318ce7", "Blond": "#faf0be", "Blue (Pantone)": "#0018a8",
                "Brilliant Rose": "#ff55a3", "British Racing Green": "#004225"}

user_colour = str(input("Enter your choice of colour: ")).title()
while user_colour != "":
    print(f"The code for color {user_colour} is {COLOUR_CODES.get(user_colour)}")
    user_colour = str(input("Enter your choice of colour: ")).title()
