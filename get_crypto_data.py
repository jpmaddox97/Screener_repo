import requests
import api_key


class GetCryptoListData:
    """Get and display cryptocurrency data. Accepts two arguments, 
    the limit which determines the amount of source data we have access to, 
    and the list of crypto symbols we want data for. All symbols must be capitals
    and stored in the list as a string.
    """

    def __init__(self, limit, crypto_list, json=''):
        # When class is called you will enter the limit and a list of tickers
        self.limit = limit
        self.crypto_list = crypto_list
        self.json = json

        # Initialize api call, api key stored in module

    def _api_call(self):
        self.limit = str(self.limit)
        headers = {
            'X-CMC_PRO_API_KEY': api_key.key,
            'Accepts': 'application/json',
        }
        # Indicate what, and what range of information we want
        params = {
            'start': '1',
            'limit': self.limit,
            'convert': 'USD',
        }
        # API url for the latest listings
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        # API call
        self.json = requests.get(url, params=params, headers=headers).json()

    def get_price(self):
        """Gets the price of the cryptos entered into class"""
        self._api_call()
        # set json dict equal to a variable
        coins = self.json['data']
        # Tickers list of cryptos we want info for
        tickers = self.crypto_list

        for x in coins:
            # Itterates through the keys in the json dict
            for t in tickers:
                # For each ticker
                if x['symbol'] == t:
                    # If the ticker is in the dictionary print the symbol and the price
                    # In the second half, since the brackets are not separated by a comma
                    # it 'digs' further into the key value pairs, the last bracket is what
                    # is actually printed
                    print(
                        f"Symbol: {x['symbol']}, Price: {round(x['quote']['USD']['price'], 4)}")

    def get_volume_24(self):
        """Gets the price of the cryptos entered into class"""
        self._api_call()
        # set json dict equal to a variable
        coins = self.json['data']
        # Tickers list of cryptos we want info for
        tickers = self.crypto_list

        for x in coins:
            # Itterates through the keys in the json dict
            for t in tickers:
                # For each ticker
                if x['symbol'] == t:
                    # If the ticker is in the dictionary print the symbol and the price
                    # In the second half, since the brackets are not separated by a comma
                    # it 'digs' further into the key value pairs, the last bracket is what
                    # is actually printed
                    print(
                        f"Symbol: {x['symbol']}, Volume 24h: {round(x['quote']['USD']['volume_24h'], 2)}")

    def get_vol24_price(self):
        """Gets the price of the cryptos entered into class"""
        self._api_call()
        # set json dict equal to a variable
        coins = self.json['data']
        # Tickers list of cryptos we want info for
        tickers = self.crypto_list

        for x in coins:
            # Itterates through the keys in the json dict
            for t in tickers:
                # For each ticker
                if x['symbol'] == t:
                    # If the ticker is in the dictionary print the symbol and the price
                    # In the second half, since the brackets are not separated by a comma
                    # it 'digs' further into the key value pairs, the last bracket is what
                    # is actually printed
                    print(
                        f"Symbol: {x['symbol']}, Price: {round(x['quote']['USD']['price'], 4)},"
                        f"Volume 24h: {round(x['quote']['USD']['volume_24h'], 2)}")

    def perc_change_h(self):
        """Percent change houly"""
        self._api_call()
        # set json dict equal to a variable
        coins = self.json['data']
        # Tickers list of cryptos we want info for
        tickers = self.crypto_list

        for x in coins:
            # Itterates through the keys in the json dict
            for t in tickers:
                # For each ticker
                if x['symbol'] == t:
                    # If the ticker is in the dictionary print the symbol and the price
                    # In the second half, since the brackets are not separated by a comma
                    # it 'digs' further into the key value pairs, the last bracket is what
                    # is actually printed
                    print(
                        f"Symbol: {x['symbol']}, Percent Change H:"
                        f" %{round(x['quote']['USD']['percent_change_1h'], 2)}")

    def perc_change_d(self):
        """Percent change daily"""
        self._api_call()
        # set json dict equal to a variable
        coins = self.json['data']
        # Tickers list of cryptos we want info for
        tickers = self.crypto_list

        for x in coins:
            # Itterates through the keys in the json dict
            for t in tickers:
                # For each ticker
                if x['symbol'] == t:
                    # If the ticker is in the dictionary print the symbol and the price
                    # In the second half, since the brackets are not separated by a comma
                    # it 'digs' further into the key value pairs, the last bracket is what
                    # is actually printed
                    print(
                        f"Symbol: {x['symbol']}, Percent Change D:"
                        f" %{round(x['quote']['USD']['percent_change_24h'], 2)}")

    def perc_change_w(self):
        """Percent change weekly"""
        self._api_call()
        # set json dict equal to a variable
        coins = self.json['data']
        # Tickers list of cryptos we want info for
        tickers = self.crypto_list

        for x in coins:
            # Itterates through the keys in the json dict
            for t in tickers:
                # For each ticker
                if x['symbol'] == t:
                    # If the ticker is in the dictionary print the symbol and the price
                    # In the second half, since the brackets are not separated by a comma
                    # it 'digs' further into the key value pairs, the last bracket is what
                    # is actually printed
                    print(
                        f"Symbol: {x['symbol']}, Percent Change W:"
                        f" %{round(x['quote']['USD']['percent_change_7d'], 2)}")

    # Add a method that checks if the symbol is present in the data

# cl = ['BTC', 'LTC', 'MANA', 'REN', 'DOGE', 'ZRX']

# if __name__ == '__main__':
#     gcld = GetCryptoListData(200, cl)
#     # gcld.get_price()
#     # gcld.get_volume_24()
#     # gcld.get_vol24_price()
#     gcld.perc_change_d()
#     gcld.perc_change_h()
#     gcld.perc_change_w()
