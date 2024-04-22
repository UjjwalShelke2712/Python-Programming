#C1-Ujjwal Shelke 84158


def function1():
    n1 = (input("Enter the set values for List1 : ")).split()
    n2 = (input("Enter the set values for List2 : ")).split()

    print(f"List1 = {n1}")
    print(f"List2 = {n2}")

    return bool(set(n1) & set(n2))


print(function1())
