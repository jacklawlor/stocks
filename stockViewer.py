#!/usr/bin/env python
'''stockViewer.py, Jack Lawlor, 20/05/2019
This programme allows the user view a stock price change over a user defined time from yahoo
'''

# importing relevant libraries
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import datetime as dt

# user input for the stock they want to view
stockName = input("Name of stock:").upper()

# user input asking how many years they want to view the change over
yrs = int(input("How many years to plot?"))

# converting inputted years to days
# note, data set does not include weekends, so take away 2 * 52
daysBack = ((365 - 104) * yrs)

# read in data from yahoo
stock = pdr.get_data_yahoo(stockName, start=dt.datetime(2000, 1, 1), end=dt.datetime.today())


def main():
    # subset dataset to be plotted
    plot = stock['Adj Close'].iloc[-daysBack:].plot()
    plt.show(plot)


if __name__ == '__main__':
    main()
