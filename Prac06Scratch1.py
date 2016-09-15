from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMToKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('Prac06Scratch1.kv')
        return self.root

    def convert_m_km(self, miles):
        kilometre = miles / 0.621
        self.root.ids.output_label.text = str(kilometre)

    def increment_miles(self, increment):
        try:
            miles = int(self.root.ids.input_miles.text) + increment
        except ValueError:
            miles = 0
        self.root.ids.input_miles.text = str(miles)

ConvertMToKm().run()



