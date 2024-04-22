# c1-83638-Ujjwal Shellke

def function_sum(n):
    if n <= 1:
        return n
    else:
        return n + function_sum(n - 1)


result = function_sum(10)  # here you can change 10 to input desired value
print(f"The sum of numbers from 1 to 10 is : {result}")
