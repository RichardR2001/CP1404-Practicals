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
        """..."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def get_fare(self):
        """..."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """..."""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"
