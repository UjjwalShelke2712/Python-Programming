# C1-84158-Ujjwal Shelke


class Product:
    def __init__(self, cname):
        print(f"Product class object = {self}")
        self.__cname = cname

    def printProductInfo(self):
        print(f"Name = {self.__cname}")


class Laptop(Product):
    def __init__(self, cname, pid, colour, price):
        print(f"Inside Laptops class Initializer {self}")
        Product.__init__(self, cname)
        self.__pid = pid
        self.__colour = colour
        self.__price = price

    def printLaptopInfo(self):
        self.printProductInfo()
        print(f"Laptop Colour = {self.__colour}")
        print(f"Laptop price = {self.__price}")
        print(f"Laptop id = {self.__pid}")


class Watch(Product):
    def __init__(self, cname, pid, colour, price):
        Product.__init__(self, cname)
        self.__pid = pid
        self.__colour = colour
        self.__price = price

    def printWatchInfo(self):
        self.printProductInfo()
        print(f"Watch id = {self.__pid}")
        print(f"Watch colour = {self.__colour}")
        print(f"Watch price = {self.__price}")


class Ipad(Product):
    def __init__(self, cname, pid, colour, price):
        Product.__init__(self, cname)
        self.__pid = pid
        self.__colour = colour
        self.__price = price

    def printIpadInfo(self):
        self.printProductInfo()
        print(f"Watch id = {self.__pid}")
        print(f"Watch colour = {self.__colour}")
        print(f"Watch price = {self.__price}")


lobj = Laptop("LENOVO", 561651651, "Black", 651615651)
lobj.printLaptopInfo()
wobj = Watch("Noise", 354315, "Grey", 2500)
wobj.printWatchInfo()
Iobj = Ipad("Apple", 3551654, "white", 65000)
