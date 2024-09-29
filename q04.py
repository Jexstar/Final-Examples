import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date #pip install datetime
from pandas import json_normalize
import requests #pip install requests
def q04():
    #q04
    # https://fakestoreapi.in/api/products
    # Histogram of price

    BASE_URL = 'https://fakestoreapi.in/'
    response = requests.get(BASE_URL + "api/products")
    data = response.json()
    df = json_normalize(data)
    df2 = json_normalize(df.products[0])
    df3 = df2.query("price < 4000")

    #print(df3[['price']])

    # output
    plt.figure(figsize=(10.4, 6.4))
    plt.hist(df3[['price']], edgecolor='white', linewidth=1.5)

    #plt.show()
    path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\Final_Sheet01\\" + 'hist04.png'
    plt.savefig(path)