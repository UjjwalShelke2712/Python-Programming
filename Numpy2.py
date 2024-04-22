# C1-84158-Ujjwal Shelke


import numpy as np


def function1():
    a1 = np.array([25, 65, 84, 56])
    a2 = np.array([54, 58, 98, 78])

    print(a1)
    print(a2)
    print(f"Addition = {a1 + a2}")
    print(f"Substraction = {a1 - a2}")
    print(f"Multiplication = {a1 * a2}")
    print(f"Divison = {a1 / a2}")


function1()

print("-" * 80)


def function2():
    a1 = np.arange(10, 22).reshape(3, 4)

    print("3x4 NumPy Array:")
    print(a1)


function2()

print("-" * 80)


def function3():
    a1 = np.eye(3)
    print(a1)


function3()

print("-" * 80)


def function4():
    a1 = np.arange(10, 22).reshape(3, 4)

    print("3x4 NumPy Array:")
    print(a1)
    num_rows, num_cols = a1.shape
    print(num_rows)
    print(num_cols)


function4()

print("-" * 80)


def function5():
    a1 = np.diag([1, 2, 3, 4, 5])
    print(a1)


function5()

print("-" * 80)


def function6():
    a1 = np.random.rand(3, 3, 3)
    print("3x3x3 NumPy Array with Arbitrary Values:")
    print(a1)


function6()

print("-" * 80)


def function7():
    a1 = np.random.rand(2, 3, 4)
    print("2x3x4 NumPy Array with Arbitrary Values:")
    print(a1)


function7()

print("-" * 80)


def function8():
    a1 = [5, 9, 6, 3, 7, 2]

    one_dim = np.array(a1)
    print(one_dim)


function8()

print("-" * 80)


def function9():
    a1 = np.arange(2, 11).reshape(3, 3)

    print("3x3 NumPy Matrix with Values Ranging from 2 to 10:")
    print(a1)


function9()

print("-" * 80)


def function10():
    a1 = np.arange(12, 39)
    print(a1)


function10()

print("-"*80)
