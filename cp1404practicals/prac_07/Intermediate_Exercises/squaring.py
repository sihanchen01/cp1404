"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Sihan Chen, IT@JCU
Started May.06.2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Sihan Chen'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 250)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()
