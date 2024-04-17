#Code By Ujjwal Shelke 84158
def calculate_average(subject1, subject2, subject3):
    """
    Calculates the average of three subject marks.

    Args:
        subject1 (float): Marks obtained in subject 1.
        subject2 (float): Marks obtained in subject 2.
        subject3 (float): Marks obtained in subject 3.

    Returns:
        float: Average marks.
    """
    total_marks = subject1 + subject2 + subject3
    return total_marks / 3

def assign_grade(average):
    """
    Assigns a grade based on the average marks.

    Args:
        average (float): Average marks.

    Returns:
        str: Grade.
    """
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

try:
    subject1 = float(input("Enter marks for subject 1: "))
    subject2 = float(input("Enter marks for subject 2: "))
    subject3 = float(input("Enter marks for subject 3: "))

    avg_marks = calculate_average(subject1, subject2, subject3)
    grade = assign_grade(avg_marks)

    print(f"Average marks: {avg_marks:.2f}")
    print(f"Grade: {grade}")
except ValueError:
    print("Invalid input. Please enter valid marks (numeric values).")
