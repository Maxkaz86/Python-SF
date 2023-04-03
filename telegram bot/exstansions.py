import json
import requests
from config import keys
class APIexception(Exception):
    pass

class Exchangeconverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise APIexception(f'Неозможно конвертировать одинаковую валюту {base}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIexception(f'Не удалось обработать валюту {quote}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIexception(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIexception(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]
        total_base = int(total_base) * int(amount)
        return total_base

