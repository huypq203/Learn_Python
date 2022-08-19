import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data_df = pd.read_csv('train.csv', index_col='Id')
print(data_df.columns)


features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = data_df[features]
y = data_df['SalePrice']

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)
