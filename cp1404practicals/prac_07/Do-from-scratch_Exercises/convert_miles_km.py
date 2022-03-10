from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = "Sihan Chen"
MILE_TO_KM = 1.60934


class MilesToKmApp(App):
    """MilesToKmApp is a Kivy app to convert miles into kilometers"""

    kilometers = StringProperty()

    def build(self):
        Window.size = (600, 300)
        self.title = "Miles to Kms Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        miles = self.root.ids.input_miles.text
        try:
            kilometers = round((float(miles) * MILE_TO_KM), 3)
            self.kilometers = str(kilometers)
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_increment(self):
        miles = self.root.ids.input_miles.text
        try:
            self.root.ids.input_miles.text = str(
                float(miles) + 1)
            self.handle_convert()
        except ValueError:
            self.root.ids.input_miles.text = "1.0"

    def handle_decrement(self):
        miles = self.root.ids.input_miles.text
        try:
            self.root.ids.input_miles.text = str(
                float(miles) - 1)
            self.handle_convert()
        except ValueError:
            self.root.ids.input_miles.text = "-1.0"


MilesToKmApp().run()
