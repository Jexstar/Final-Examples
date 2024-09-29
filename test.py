import pandas as pd
import matplotlib.pyplot as plt

path = "C:\\Users\\ADMIN\\Desktop\\transactions.csv"

df = pd.read_csv(path)

df2 = df[df['shippingCountry'].notnull()]
df3 = df2.query('shippingCountry == "US"')
df3['shippingState'] = df3['shippingState'].fillna("null")

#print(df3.isna().sum())
state_list = []
for x in df3.index:
    state_list.append(df3.at[x, 'shippingState'])
state_list2 = list(dict.fromkeys(state_list))

num_transactions_state = []
for x in state_list2:
    df_state3 = df3[df3['shippingState'] == x]
num_transactions = len(df_state3)
print(num_transactions)
num_transactions_state.append(num_transactions)
plt.figure(figsize=(20.4, 6.4))
plt.bar(state_list2, num_transactions_state)
plt.show()
# df3['shippingState'] = df3['shippingState'].fillna('N/A')
# print(df3.head())