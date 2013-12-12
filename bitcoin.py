from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout

from conversor import BitcoinCalculator


class BitcoinApp(App):

    def _convert(self, amount):

        return "%s BTC" % self.bitcoin_calculator.convert(amount)
        
    def convert(self, *args):

        self.results_label.text = self._convert(self.amount_input.text)

    def change_currency(self, btn):
        
        self.bitcoin_calculator.update(currency=btn.text)

    def load_currencies(self):

        for currency in self.bitcoin_calculator.currencies():

            btn = Button(text=currency, size_hint_y=None, height=44)
            btn.bind(on_release=self.change_currency)
            self.currencies_combo.add_widget(btn)

    def build(self):

        layout = GridLayout(cols=3)

        self.convert_button = Button(text="Convert", on_press=self.convert, font_size=20)
        self.amount_input = TextInput(text="1")
        self.results_label = TextInput(text="")
        self.currencies_combo = DropDown()

        self.update_button = Button(text="Update", on_press=self.convert, font_size=20)

        layout.add_widget(self.update_button)
        layout.add_widget(self.amount_input)
        layout.add_widget(self.currencies_combo)
        layout.add_widget(self.convert_button)
        layout.add_widget(self.results_label)

        return layout

    def on_start(self):

        self.bitcoin_calculator = BitcoinCalculator()
        self.load_currencies()


BitcoinApp().run()