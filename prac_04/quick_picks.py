"""
CP1404 - Practical 4
Quick Picks
Created on 3/12/21 by Richard Reynard
"""
import random

NUMBERS_IN_A_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    user_number = int(input("How many quick picks? "))
    while user_number < 0:
        print("Invalid input")
        user_number = int(input("How many quick picks? "))

    for i in range(user_number):
        quick_pick = []
        for j in range(NUMBERS_IN_A_LINE):
            number_generated = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number_generated in quick_pick:
                number_generated = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(number_generated)
        quick_pick.sort()
        print(" ".join("{:2}".format(number_generated) for number_generated in quick_pick))


main()
