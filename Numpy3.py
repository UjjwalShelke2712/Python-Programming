# C1-84158-Ujjwal Shelke


import numpy as np


def function1():
    a1 = np.array([25, 12, 65, 95, 75, 36, 45, 11, 2, 6, 8])

    rev_a1 = a1[::-1]

    print(rev_a1)


function1()

print("-" * 80)


def function2():
    a1 = np.array([11, 22, 33, 44, 55, 66], dtype=np.float16)

    print(a1)


function2()

print("-" * 80)


def function3():
    a1 = [[1, 2, 3, 4],
          [5, 6, 7, 8]]
    print(a1)

    a2 = np.array(a1)
    print(a2)


function3()

print("-" * 80)


def function4():
    a1 = np.array([52, 96, 85, 35, 61, 73, 93, 43])
    print(f"divison is {a1 / 2}")
    print(f"remainder is {a1 % 2}")


function4()

print("-" * 80)


def function5():
    a1 = np.arange(20, 51)
    print(a1)
    print(f"divison is {a1 / 3}")
    print(f"remainder = {a1 % 3}")


function5()
