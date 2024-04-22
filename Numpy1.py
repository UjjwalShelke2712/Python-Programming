# C1-Ujjwal Shelke

import numpy as np



def function1():
    arr = np.array([1, 7, 13, 105])

    memory_size = arr.nbytes

    print(f"NumPy Array:")
    print(arr)
    print(f"Memory occupied by the array:", {memory_size}, "bytes")


function1()

print("-" * 80)


def function2():
    a1 = np.array([50, 20, 54, 85])
    a2 = np.array([36, 59, 86, 32])

    print(f"a1 = {a1}")
    print(f"a2 = {a2}")
    print(f"a1>a2 = {a1 > a2}")
    print(f"a1>a2 = {a2 > a1}")
    print(f"a1>a2 = {a1 >= a2}")
    print(f"a1>a2 = {a2 >= a1}")


function2()

print("-" * 80)


def function3():
    a1 = np.zeros(10)
    print(f"{a1}")
    a2 = np.ones(10)
    print(f"{a2}")
    a3 = np.ones(10) * 5
    print(f"{a3}")
    a4 = np.ones(10) * 10
    print(f"{a4}")
    a5 = np.ones(10) * 20
    print(f"{a5}")
    a6 = np.ones(10) * 50
    print(f"{a6}")


function3()

print("-" * 80)


def function4():
    a1 = np.arange(30, 71, 1)
    print(a1)


function4()

print("-" * 80)


def function5():
    a1 = np.arange(50, 96, 1)
    print(a1)


function5()

print("-" * 80)


def function6():
    a1 = np.arange(20, 81, 2)
    print(a1)


function6()

print("-" * 80)


def function7():
    a1 = np.arange(19, 80, 2)
    print(a1)


function7()

print("-" * 80)


def function8():
    a1 = np.random.randint(10, 41, 15)
    print(a1)


function8()

print("-" * 80)


def function9():
    a1 = np.random.randint(30, 50, 10)
    print(a1)


function9()

print("-" * 80)


def function10():
    a1 = np.random.randint(50, 90, 20)
    print(a1)


function10()

print("-" * 80)
