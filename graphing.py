#importing libraries 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('csv_files/train.csv')
sale_prices = data.iloc[:,-1].values
mean = np.mean(sale_prices)
std = np.std(sale_prices)
print(max(sale_prices))
print(min(sale_prices))
print(mean)
print(std)


import scipy.stats as stats
import math
x = np.linspace(mean - 3*std, mean + 5*std, 100)
plt.plot(x, stats.norm.pdf(x, mean, std))
plt.show()

