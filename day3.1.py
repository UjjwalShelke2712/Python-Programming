# C1-Ujjwal Shelke 84158

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


digit = 11   # remove 11 and write input function for taking input from user

for i in range(digit):
    print(f"The factorial of {i} is {factorial(i)}")
