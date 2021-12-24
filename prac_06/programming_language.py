"""
CP1404 - Practical 6
Created on 24 December 2021 by Richard Reynard
"""


class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, field="", typing="", reflection="", year=0):
        """Initialise a programming language instance"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year


