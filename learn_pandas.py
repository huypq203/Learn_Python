import numpy as np
import pandas as pd

df = pd.read_csv("chipotle.tsv", sep='\t')
print(df.head(5))

print(df.shape)

print(list(df.columns))

print(df.info())

print(df.index)

print(df.describe(include='all'))

print(df.loc[(df.quantity == 15) | (df.item_name == 'Nantucket Nectar'), ['order_id', 'quantity', 'item_name']])

print(type(df.iloc[[9]]))

x = df.iloc[3:11, :-1]
print(x)

print(df.item_price.dtype)

print(df.item_price.apply(lambda x : float(x.replace('$', ''))).dtype)

df.item_price = df.item_price.apply(lambda x : float(x.replace('$', '')))

print(df.head())

df['total_price'] = df['quantity'] * df['item_price']

print(df.head())

print(df.total_price.sum())

print(df.groupby('item_name')['quantity'].sum())
c = df.groupby('item_name')['quantity'].sum()
print(c.sort_values(ascending=False).head(5))

print(df.item_name.value_counts().count())
print(df.item_name.nunique())
