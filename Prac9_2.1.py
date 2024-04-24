import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plot1
df = pd.read_csv('./Advertising.csv')

tv = df['TV']
sales = df['sales']
newspaper = df['newspaper']
radio = df['radio']

plt.subplot(1,3,1)
plt.bar(tv,sales)


plt.subplot(1,3,2)
plt.bar(radio,sales)

plt.subplot(1,3,3)
plt.bar(newspaper,sales)

plt.show()