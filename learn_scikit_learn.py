import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


data_df = pd.read_csv('Data.csv')
print(data_df.head())


# Data Imputation
print(data_df.info())
for col in data_df.columns:
    missing_data = data_df[col].isna().sum()
    missing_percent = missing_data/len(data_df) * 100
    print(f'Column {col} has {missing_percent}% missing percent')

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(data_df.isna(), cmap='Blues', cbar=False, yticklabels=False)

X = data_df.iloc[:,:-1].values
y = data_df.iloc[:,-1].values

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


# Encode Categorical Data
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = ct.fit_transform(X)
print(X)

le = LabelEncoder()
y = le.fit_transform(y)
print(y)


# Split dataset
np.random.seed(42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# Feature scaling
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:,3:])
X_test[:, 3:] = sc.fit(X_test[:, 3:])


plt.show()


