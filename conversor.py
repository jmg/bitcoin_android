import urllib2
import json

from kivy.storage.jsonstore import JsonStore


class BitcoinCalculator(object):

    DEFAULT_CURRENCY = "USD"
    BITCOIN_URL = "http://blockchain.info/ticker"
    store = JsonStore("prices.json")

    def __init__(self):

        try:
            self.update()
        except:
            print "Seems like you don't have access to an internet connection. Using the last stored price for convertions"

    def _get_prices(self):

        if "prices" in self.store:
            return self.store.get("prices")
            
        content = urllib2.urlopen(self.BITCOIN_URL).read()
        prices = json.loads(content)
        self.store["prices"] = prices

        return prices

    def _get_price(self, currency):

        price = self._get_prices()[currency]["buy"]
        return float(price)

    def convert(self, amount):

        return float(amount) / self.price

    def currencies(self):

        return self._get_prices().keys()

    def update(self, currency=DEFAULT_CURRENCY):

        self.price = self._get_price(currency)