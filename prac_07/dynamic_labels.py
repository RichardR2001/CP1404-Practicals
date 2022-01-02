"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create labels based on content of dictionary
Created on 02-01-2022 by Richard Reynard
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ['Alexander', 'Daryl', 'Jessica', 'Riley']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.name_list:
            label_name = Label(text=name)
            self.root.ids.main.add_widget(label_name)


DynamicLabelsApp().run()
