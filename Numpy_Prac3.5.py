# C1-84158-Ujjwal Shelke


class Product:
    def __init__(self, cname):
        self.__cname = cname

    def get_cname(self):
        return self.__cname

    def set_cname(self, cname):
        self.__cname = cname

class Laptop(Product):
    def __init__(self, pid, price, colour, cname):
        Product.__init__(self, cname)
        self.__pid = pid
        self.__price = price
        self.__colour = colour

    def get_pid(self):
        return self.__pid

    def set_pid(self, pid):
        self.__pid = pid

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

class Watch(Product):
    def __init__(self, pid, price, colour, cname):
        Product.__init__(self, cname)
        self.__pid = pid
        self.__price = price
        self.__colour = colour

    def get_pid(self):
        return self.__pid

    def set_pid(self, pid):
        self.__pid = pid

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

class iPad(Product):
    def __init__(self, pid, price, colour, cname):
        Product.__init__(self, cname)
        self.__pid = pid
        self.__price = price
        self.__colour = colour

    def get_pid(self):
        return self.__pid

    def set_pid(self, pid):
        self.__pid = pid

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

class Bill:
    def __init__(self):
        self.__laptop_list = []
        self.__watch_list = []
        self.__ipad_list = []

    def add_laptop(self, laptop):
        self.__laptop_list.append(laptop)

    def add_watch(self, watch):
        self.__watch_list.append(watch)

    def add_ipad(self, ipad):
        self.__ipad_list.append(ipad)

    def calculate_total_bill(self):
        total_bill = 0
        for laptop in self.__laptop_list:
            quantity = int(input("Enter quantity of laptop: "))
            total_bill += laptop.get_price() * quantity

        for watch in self.__watch_list:
            quantity = int(input("Enter quantity of watch: "))
            total_bill += watch.get_price() * quantity

        for ipad in self.__ipad_list:
            quantity = int(input("Enter quantity of ipad: "))
            total_bill += ipad.get_price() * quantity

        return total_bill

laptop1 = Laptop(1, 50000, "black", "laptop")

watch1 = Watch(1, 2000, "black", "watch")

ipad1 = iPad(1, 15000, "black", "ipad")

bill = Bill()
bill.add_laptop(laptop1)
bill.add_watch(watch1)
bill.add_ipad(ipad1)

print("Total bill: ", bill.calculate_total_bill())
