# importar as bibliotecas a serem utilizadas
import time
import webbrowser
import selenium
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

url="https://br.investing.com/etfs/world-etfs?&issuer_filter=0"
webbrowser.open(url, new = 2)


