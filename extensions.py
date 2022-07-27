import requests
import json
from config import keys


class APIException(Exception):
    pass

class get_price:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты:  {base}🤯')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Введена неправильная или несуществующая валюта:  {quote}🤯')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Введена неправильная или несуществующая валюта:  {base}🤯')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неправильно введено число:  {amount}🤯')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]*amount

        return total_base