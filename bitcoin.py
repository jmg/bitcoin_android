import urllib2
import json

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout


class BitcoinApp(App):

    DEFAULT_CURRENCY = "USD"
    BITCOIN_URL = "http://blockchain.info/ticker"

    def _get_price(self, currency=None):

        if currency is None:
            currency = self.DEFAULT_CURRENCY

        content = urllib2.urlopen(self.BITCOIN_URL).read()
        return json.loads(content)[currency]["buy"]

    def _convert(self, amount, currency=None):

        price = self._get_price(currency=currency)
        value = float(str(amount)) / float(price)

        print value
        
    def convert(self, *args):

        self._convert(self.amount_input.text)

    def build(self):

        root = GridLayout()
        layout = FloatLayout(orientation='horizontal', size=(450,300), size_hint=(None, None))

        self.convert_button = Button(text="Convert", on_press=self.convert, pos=(300,300),font_size=20)
        self.amount_input = TextInput(text="1")

        layout.add_widget(self.convert_button)
        layout.add_widget(self.amount_input)

        root.add_widget(layout)
        return root


BitcoinApp().run()