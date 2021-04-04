import requests
import time
from config import *

data = requests.get(url).json()
# while (1):
currencyData = dict()
for ticker in data["tickers"]:
    # if abs(ticker['todaysChangePerc']) > 1:
    print("Today", ticker['ticker'][2:], "Changed", ticker['todaysChangePerc'])
    name = ticker['ticker'][2:]
    if name not in currencyData:
        currencyData[name] = ticker['lastQuote']['b']
    percentChanged = ((currencyData[name] -
                       ticker['lastQuote']['b'])/ticker['lastQuote']['b'])*100
    if abs(percentChanged) >= 1:
        print(ticker['ticker'][2:], "changed ", percentChanged)
    currencyData[ticker['ticker'][2:]] = ticker['lastQuote']['b']
# time.sleep(60)
