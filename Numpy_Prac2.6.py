# C1-84158_Ujjwal Shelke

from functools import reduce

def fun():
    n = int(input())
    l1 = []
    for i in range(n):
        num = int(input("Enter Value : "))
        l1.append(num)
    print(l1)
    add = lambda a, b : a * b
    res = reduce(add,l1)
    print(res)

fun()