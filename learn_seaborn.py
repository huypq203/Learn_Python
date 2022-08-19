import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())
sns.set_theme()

tips_df = sns.load_dataset('tips')
print(tips_df.head())


# Distribution: hist, KDE

# sns.histplot(data=tips_df['total_bill'])
# print(tips_df['total_bill'].value_counts().sort_values(ascending=False))

# sns.kdeplot(data=tips_df['total_bill'])

# sns.displot(data=tips_df, x='total_bill', col='time', kde=True) # need hist or kde before


# Bar plot
# sns.barplot(data=tips_df, x='sex', y='tip', estimator=np.mean)


# Count plot
# print(tips_df['sex'].value_counts())
# sns.countplot(data=tips_df, x='sex')


# Box plot
# sns.boxplot(data=tips_df, x='day', y='total_bill', hue='sex', palette='Reds')
# plt.xlabel('Day')
# plt.ylabel('Total Bill')
# plt.legend(loc=0)


# Facet Grid
# kws = dict( s=100, edgecolor='b', alpha=0.7 )
# tips_fig = sns.FacetGrid(data=tips_df, row='smoker', col='time', hue='sex', palette='Set2', height=4, aspect=1.4) # need a plot before
# tips_fig.map(sns.scatterplot, 'total_bill', 'tip', **kws)
# tips_fig.add_legend()


penguins_df = sns.load_dataset('penguins')
print(penguins_df.head())


# Join Plot
# sns.jointplot(data=penguins_df, x='flipper_length_mm', y='bill_length_mm', hue='species')


# Pair Plot
# sns.pairplot(data=penguins_df, hue='species') # need a plot before


# Heat Map


flights_df = sns.load_dataset('flights')
print(flights_df.head())


flights = pd.pivot_table(flights_df, index='month', columns='year', values='passengers')
print(flights)


sns.heatmap(data=flights, cmap='Blues', linewidths=1)

plt.show()
