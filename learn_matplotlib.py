import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print(plt.style.available)
plt.style.use('seaborn-white')

# x = [ 1, 2, 3 ,4 ]
# y = [ 10, 8, 6, 9 ]
# plt.plot(x, y)


# Pyplot API

# x = np.linspace(0, 10, 1000)
# plt.plot(x, np.sin(x), color='blue', linestyle='dashed', label='sin(x)')
# plt.plot(x, np.cos(x), color='red', label='cos(x)')
# plt.title('sin(x) and cos(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# # plt.xlim([0, 4])
# # plt.axis([ 0, 4, -0.7, 0.6 ])
# # plt.axis('tight')
# # plt.axis('equal')


# Object-Oriented API

# x = [ 1, 2, 3, 4 ]
# y = [ 11, 22, 33, 44 ]

# fig, ax = plt.subplots(figsize=(5,5))
# ax.plot(x, y)

# ax.set(title='A simple plot',
#         xlabel='x',
#         ylabel='y')


# Most common type of Matplotlib plots
# line, scatter, bar, hist, subplots()

# x = np.linspace(0,10,1000)
# plt.scatter(x, np.exp(x))


# rng = np.random.RandomState(0)

# x = np.random.randn(100)
# y = np.random.randn(100)

# colors = rng.rand(100)
# sizes = 1000*rng.rand(100)

# fig, ax = plt.subplots()
# img1 = ax.scatter(x,y,s=sizes,c=colors,cmap='viridis', alpha=0.3)
# fig.colorbar(img1)


# soft_drink_prices = { 'Coke' : 10, 'Pessi' : 12, 'Sprite' : 8 }
# fig, ax = plt.subplots()

# # ax.bar(soft_drink_prices.keys(), soft_drink_prices.values())
# # ax.set(title='Grocery', ylabel='Prices')

# # ax.barh(list(soft_drink_prices.keys()), list(soft_drink_prices.values()))
# # ax.set(title='Grocery', xlabel='Prices')


# student_height = np.random.normal(170, 10, 250)

# # plt.hist(student_height, bins=30)

# # fig, ax = plt.subplots()
# # ax.hist(student_height)


# Subplots

# fig, ( ( ax1, ax2 ), ( ax3, ax4 ) ) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
# x = np.linspace(0,10,1000)
# soft_drink_prices = { 'Coke' : 10, 'Pessi' : 12, 'Sprite' : 8 }
# student_height = np.random.normal(170, 10, 250)
# ax1.plot(x, x/2)
# ax2.scatter(np.random.random(100), np.random.random(100))
# ax3.bar(soft_drink_prices.keys(), soft_drink_prices.values())
# ax4.hist(student_height, bins=30)

# fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
# x = np.linspace(0,10,1000)
# soft_drink_prices = { 'Coke' : 10, 'Pessi' : 12, 'Sprite' : 8 }
# student_height = np.random.normal(170, 10, 250)
# ax[0, 0].plot(x, x/2)
# ax[1, 0].scatter(np.random.random(100), np.random.random(100))
# ax[0, 1].bar(soft_drink_prices.keys(), soft_drink_prices.values())
# ax[1, 1].hist(student_height, bins=30)



# plt.legend()
plt.show()

