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
    while user_choice != "q":
        if user_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")
        elif user_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                trip_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_fare}")
                total_fare = total_fare + trip_fare
            else:
                print("You need to choose a taxi before you can drive")





main()
