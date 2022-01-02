"""
CP1404 - Kivy
Created on 31-12-2021 by Richard Reynard
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class DistanceConverter(App):
    """Distance Converter will convert the user's input in miles and convert to kilometres."""
    def build(self):
        """Build the app from kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self):
        """Convert the user input to kilometres."""
        input_value = self.get_valid_miles()
        result = input_value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Add or subtract the miles value by 1."""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """Check the value input by user."""
        try:
            value = float(self.root.ids.input_miles.txt)
            return value
        except ValueError:
            return 0


DistanceConverter().run()
