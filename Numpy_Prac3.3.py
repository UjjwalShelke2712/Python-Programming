# C1-84158-Ujjwal Shelke


class Product:
    def __init__(self, name, pid):
        print(f"Product class object = {self}")
        self.__name = name
        self.__pid = pid

    def printProductInfo(self):
        print(f"Name = {self.__name}")
        print(f"Product ID = {self.__pid}")


class Laptop(Product):
    def __init__(self, name, pid, ram, storage):
        print(f"Inside Laptops class Initializer {self}")
        Product.__init__(self, name, pid)
        self.__ram = ram
        self.__storage = storage

    def printLaptopInfo(self):
        self.printProductInfo()
        print(f"Laptop ram = {self.__ram}")
        print(f"Laptop Storage = {self.__storage}")


lobj = Laptop("LENOVO", "561FCF651651", "8GB", "2TB")
lobj.printLaptopInfo()
