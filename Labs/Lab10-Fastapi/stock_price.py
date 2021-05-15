from iexfinance.stocks import Stock

# Enter your API Token here
token = 'pk_5253fd57e258481480f431fe9ac5100b'

def fetch_current_price(stock_ticker):

    a = Stock(stock_ticker, token=token)
    return a.get_quote()['latestPrice'][0]

#uvicorn print(fetch_current_price('AAPL'))
