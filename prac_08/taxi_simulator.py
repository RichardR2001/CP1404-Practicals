"""
CP1404 - Taxi Simulator
Created on 11-01-2022 by Richard Reynard
"""

from CP1404.prac_08.car import Car
from CP1404.prac_08.taxi import Taxi
from CP1404.prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """..."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").lower()





main()