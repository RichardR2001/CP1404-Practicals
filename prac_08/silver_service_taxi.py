"""
CP1404 - Practical
Silver Service Taxi
"""

from CP1404.prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """..."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """..."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

