# C1-84158-Ujjwal Shelke

class Student:
    def __init__(self, rollno, studentName, course):
        self.rollno = rollno
        self.studentName = studentName
        self.course = course
        self.marks = {}

    def __str__(self):
        return f"Roll No: {self.rollno}, Name: {self.studentName}, Course: {self.course}, Marks: {self.marks}"

    def acceptStudentData(self):
        for i in range(5):
            subjectName = input(f"Enter subject name for student {i + 1}: ")
            marks = int(input(f"Enter marks for subject {subjectName} for student {i + 1}: "))
            self.marks[subjectName] = marks

    def printStudentData(self, rollno):
        for student in students:
            if student.rollno == rollno:
                print(student)


students = []

for i in range(1):
    rollno = int(input(f"Enter roll no for student {i + 1}: "))
    studentName = input(f"Enter name for student {i + 1}: ")
    course = input(f"Enter course for student {i + 1}: ")

    student = Student(rollno, studentName, course)
    student.acceptStudentData()
    students.append(student)

rollno = int(input("Enter roll no for student to be searched: "))
student.printStudentData(rollno)
