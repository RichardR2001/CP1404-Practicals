"""
CP1404/CP5632 - Practical
Broken program to determine score status
Created on 27-11-21 by Richard Reynard
"""


def main():
    """Get score from user and determine the result"""
    score = float(input("Enter score: "))
    print(determine_grades(score))


def determine_grades(score):
    """Determine grade based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
