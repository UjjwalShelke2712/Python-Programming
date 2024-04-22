# C1-84158-Ujjwal Shelke

class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.__month = month
        self.__year = year

    def acceptDate(self):
        self.day = int(input("Enter day"))
        self.__month = int(input("Enter month"))
        self.__year = int(input("Enter month"))

    def validateDate(self):
        if self.day == 19:
            if self.__month == 2:
                if (self.__year == 2018):
                    print("Valid date is:")
                else:
                    print("Invlaid date year")
            else:
                print("Invlaid date month")
        else:
            print("Invlaid date day")

    def print1(self):
        mon = "a"
        if self.__month == 1:
            mon = "Jan"

        elif self.__month == 2:
            mon = "Feb"

        elif self.__month == 3:
            mon = "March"
        elif self.__month == 4:
            mon = "April"
        elif self.__month == 5:
            mon = "May"
        elif self.__month == 6:
            mon = "June"
        elif self.__month == 7:
            mon = "July"
        elif self.__month == 8:
            mon = "Aug"
        elif self.__month == 9:
            mon = "Sep"

        elif self.__month == 10:
            mon = "Oct"

        elif self.__month == 11:
            mon = "Nov"
        elif self.__month == 12:
            mon = "Dec"
        else:
            print("Invalid Month")

        print(f"Date is {self.day} {mon} {self.__year}")

    def setmonth(self, m):
        self.__month = m

    def setyear(self, y):
        self.__year = y

    # def getday(self):
    #   return f"{self.__day}"

    def getmonth(self):
        return f"{self.__month}"

    def getyear(self):
        return f"{self.__year}"

    def __del__(self):
        pass


d1 = Date(10, 5, 2000)

d1.acceptDate()
print("-" * 80)
d1.validateDate()
d1.print1()
