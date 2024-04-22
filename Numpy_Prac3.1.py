# C1-84158-Ujjwal Shelke

class Product:
    def __init__(self, proname, pid, cost):
        self.__proname = proname
        self.__pid = pid
        self.__cost = cost

    def get_proname(self):
        return self.__proname

    def set_proname(self, proname):
        self.__proname = proname

    def get_pid(self):
        return self.__pid

    def set_pid(self, pid):
        self.__pid = pid

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def cal_price(self, quantity):
        total_price = quantity * self.__cost
        return total_price


p = Product("Laptop", 1001, 100000)
quantity = int(input("Enter quantity: "))
print("Total price: ", p.cal_price(quantity))
