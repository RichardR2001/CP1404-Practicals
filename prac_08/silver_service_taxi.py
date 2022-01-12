"""
CP1404 - Practical
Silver Service Taxi
"""

from CP1404.prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi is an app to calculate the fare and display the fare based on the price per km and
       fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def get_fare(self):
        """Return a string that calculates the taxi fare."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string that shows the taxi name and total fare"""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"
