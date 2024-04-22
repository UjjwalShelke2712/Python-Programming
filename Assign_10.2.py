# C1-84158-Ujjwal Shelke

class Matrix():
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def accept(self):
        self.__a=int(input("Enter a"))
        self.__b = int(input("Enter b"))

    def add(self):
        ao=(self.__a)+(self.__b)
        print(f"Additon={ao}")

    def sub(self):
        so=(self.__a)-(self.__b)
        print(f"Subtraction={so}")

    def mul(self):
        mo=(self.__a)*(self.__b)
        print(f"Multiplication={mo}")




    def print1(self):
        print(f"a={self.__a} b={self.__b}")




m1=Matrix(10,20)
m1.accept()
m1.print1()
m1.add()
m1.sub()
m1.mul()