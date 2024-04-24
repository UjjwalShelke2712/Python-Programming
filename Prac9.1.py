# C1-84158-Ujjwal Shelke

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def f1():
    df = pd.read_csv('./Advertising.csv')
    print(df.head())
    print("-" * 80)
    print(df.head(20))
    print("-" * 80)
    print(df.tail(15))
    print("-" * 80)
    print(df.info)
    print("-" * 80)
    #tv = np.array([df['TV']])
    #print(tv)
    #sales = np.array([df['sales']])
    #print(sales)
    #plt.scatter(tv, sales)
    plt.scatter(df['TV'],df['sales'],color='red',label='sales')
    plt.style.use('ggplot')
    plt.xlabel("TV")
    plt.ylabel("sales")
    plt.legend()
    plt.savefig("TVSALES.png")
    plt.show()

