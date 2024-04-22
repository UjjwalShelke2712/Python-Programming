# C1-84158-Ujjwal Shelke

class Course:
    def __init__(self, name, fees):
        self.__name = name
        self.fees = fees

    def accept1(self):
        self.__name = input("Enter name")
        self.fees = int(input("Enter fees"))

    def print1(self):
        print(f"Name = {self.__name} \n Fees ={self.fees}")

    def getname(self):
        self.__name

    def getfees(self):
        return self.fees


# c1=Course("name","fees")
# c1.accept1()
# c1.print1()

class Computer(Course):
    def __init__(self, name, fees, subjectList):
        Course.__init__(self, name, fees)
        self.__subjectList = []

    def accept2(self):
        n = int(input("Enter number of subjects in Comp"))
        for i in range(1, n + 1):
            subject_name = input("Enter subject name")
            self.__subjectList.append(subject_name)

    def print2(self):
        print(f"1st year Comp {self.getfees()} {self.__subjectList}")


class Electronic(Course):
    def __init__(self, name, fees, subjectList):
        Course.__init__(self, name, fees)
        self.__subjectList = []

    def accept3(self):
        n = int(input("Enter number of subjects in Electronics"))
        for i in range(1, n + 1):
            subject_name = input("Enter subject name")
            self.__subjectList.append(subject_name)

    def print3(self):
        print(f"1st year Electronic {self.getfees()} {self.__subjectList}")


choice = int(input("ENter your choice 1 or 2 ="))
if choice == 1:
    st = Computer("n", 90000, ['sub1' 'sub2'])
    st.accept2()
    st.print2()
elif choice == 2:
    st = Electronic("n", 90000, ['sub1' 'sub2'])
    st.accept3()
    st.print3()

else:
    print("Invalid Input")
