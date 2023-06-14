import requests
import json
from Config import values


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException(f'Одинаковые валюты: {base}={quote} /help')

        try:
            base_ticker = values[base]
        except KeyError:
            raise APIException(f'Валюта не принята = {base}? /help')

        try:
            quote_ticker = values[quote]
        except KeyError:
            raise APIException(f'Валюта не принята = {quote}? /help')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Количество не принято = {amount} /help')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        result = json.loads(r.content)[values[quote]]
        result *= amount

        return result