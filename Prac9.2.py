# C1-84158-Ujjwal Shelke

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def f1():
    df = pd.read_csv('./Advertising.csv')
    plt.scatter(df['TV'], df['sales'], color='red', label='sales')
    plt.show()

#f1()

def f2():
    df = pd.read_csv('./Advertising.csv')
    plt.scatter(df['radio'], df['sales'], color='red', label='sales')
    plt.show()

#f2()


def f3():
    df = pd.read_csv('./Advertising.csv')
    plt.scatter(df['newspaper'], df['sales'], color='red', label='sales')
    plt.show()

f3()