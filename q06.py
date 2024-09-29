import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests

def q06():
    #Pie Chart

    BASE_URL = 'https://fakestoreapi.in/'
    response = requests.get(BASE_URL + "api/products")
    data = response.json()
    df = json_normalize(data)
    df2 = json_normalize(df.products[0])

    category_list = []
    for x in df2.index:
        category_list.append(df2.at[x, 'category'])
    # Remove the duplication
    category_list2 = list(dict.fromkeys(category_list))

    # print(category_list2)
    num_product_category = []
    for x in category_list2:
        df_state2 = df2[df2['category'] == x]
        num_product = len(df_state2)
        #print("Product in " + x + " is " + str(num_product) + ".")
        num_product_category.append(num_product)

     # output
    # make data
    x = [1, 2, 3, 4]
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

    # plot
    fig, ax = plt.subplots()
    ax.pie(num_product_category, labels=category_list2, colors=colors, radius=3, center=(4, 4),
            wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    # to add percentage
    # ax.pie(num_product_category, labels=category_list2, colors=colors, radius=3, center=(4, 4),
    #        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True,
    #        autopct='%1.1f%%')  # Add percentage with one decimal place

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))

    #plt.show()
    #path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\Final_Sheet01\\" + 'pie06.png'
    #plt.savefig(path)


