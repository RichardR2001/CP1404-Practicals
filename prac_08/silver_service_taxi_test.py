"""
CP1404 - Practical
Silver Service Taxi
"""

from CP1404.prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Calculate the fare of SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Hummer", 100, 4)
    taxi.drive(20)
    print(taxi)
    print(f"Total fare: ${taxi.get_fare()}")


main()
