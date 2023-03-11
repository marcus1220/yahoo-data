import numpy as np
import pandas as pd
import matplotlib as plt
import yfinance as yf
import seaborn as sns
import plotly.express as px
import datapane as dp

stock_name = input("which stock you are looking for: ")
stock = yf.Ticker(stock_name)
print (stock.history(period = "max"))
stock = yf.download(stock_name,period = "MAX",interval = "1d")
#type of chart of stock
stock_close_chart = px.line(stock["Close"],title=stock_name + " daily close price",color_discrete_map={"Close":"green"},width=800,height=800)
stock_volume_chart = px.area(stock["Volume"],title=stock_name + " daily Volume",color_discrete_map={"Volume":"red"},width=800,height=800)
stock_pct_change_inception = stock["Close"]/stock["Close"].iloc[0]
stock_pct_change_chart = px.area(stock_pct_change_inception, title=stock_name + " daily closing price", width=800,height=800)
print(stock_pct_change_inception.head())


x = 0
while x == 0:
    choice = input("1 for " + stock_name + " closing price,\n2 for " +stock_name + " volume,\n3 for " +stock_name + " closing price in %\n")

    if choice == "1":
        stock_close_chart.show()
        break
    elif choice == "2":
        stock_volume_chart.show()
        break
    elif choice == "3":
        stock_pct_change_chart.show()
        break
    else:
        print("please type a 1 2 or 3")

