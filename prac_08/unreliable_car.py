"""
CP1404 - Programming 2
Unreliable Car
Created on 07-01-2022 by Richard Reynard
"""

from CP1404.prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of car that is unreliable."""

    def __init__(self, name, fuel, reliability):
        """..."""
        super().__init__(name, fuel)
        self.reliability = reliability

    
