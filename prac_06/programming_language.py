"""
CP1404 - Practical 6
Created on 24 December 2021 by Richard Reynard
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamic typing or it is not."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representing a particular language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
