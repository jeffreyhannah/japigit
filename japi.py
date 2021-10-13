import sys
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

API_KEY = 'FXJTZJPACVPWD2K8'

def getStockdata(symbol):

    try:

        print("Searching for stock price")

        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:

        return "not found"

def main():

    outFile = open('japi.out', 'w')

    while 1:

        userInput = input("Enter Stock Symbol or EXIT to exit: ").upper()

        if userInput != "EXIT":

            serverData = 'The current price of {} is {}\n'.format(userInput, getStockdata(userInput))

            print(serverData)

            outFile.write(serverData)

        else:

            sys.exit("\nStock Quotes retrieved successfully!\n")
main()