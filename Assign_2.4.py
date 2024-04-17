#code By Ujjwal Shelke
def is_leap_year(year):
    """
    Determines if a given year is a leap year.

    Args:
        year (int): The input year.

    Returns:
        str: A string indicating whether the year is a leap year or not.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "NOT a Leap Year"

# Example usage:
try:
    user_input = int(input("Enter a year: "))
    result = is_leap_year(user_input)
    print(f"{user_input} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid year.")
