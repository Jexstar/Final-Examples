import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def q02():
# Requirements
# - Average VISA transaction amounts by shipping country
# - barh()
# - size 6.4 x 50.4
# - Please do not forget uppercase shipping country letters
    path = "C:\\Users\\ADMIN\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\transactions.csv"
    df = pd.read_csv(path)
    df2 = df[df['shippingCountry'].notnull()] #filter null value
    df3 = df2.query("cardType == 'VISA'")

    # country_list = []
    # for x in df3.index:
    #     country_list.append(df3.at[x, 'shippingCountry'])
    # # Remove the duplication
    # country_list2 = list(dict.fromkeys(country_list))
    # #print(country_list2)
# Extract the unique values of 'shippingCountry' into a list
    country_list2 = df3['shippingCountry'].unique().tolist()


    amount_transactions_country = []
    for x in country_list2:
        df_country3 = df3[df3['shippingCountry'] == x]
        average_transactions = df_country3[['transactionAmountUSD']].to_numpy().mean()
        #print("Transactions in " + x + " is " + str(amount_transactions) + ".")
        amount_transactions_country.append(average_transactions)

    # output file
    plt.figure(figsize=(6.4, 50.4))
    plt.barh(country_list2, amount_transactions_country)
    #plt.show()
    path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\Final_Sheet01\\" + 'bar02.png'
    plt.savefig(path)