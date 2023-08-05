print("Olá mundo")
print("Teste python")
print("ok")
import yfinance as yf
import pandas as pd
ticker = ("PETR4.SA","BBDC4.SA")
data = yf.download(ticker, start="2022-01-01", end="2023-01-01")
print (data)