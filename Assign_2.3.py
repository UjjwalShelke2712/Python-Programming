#code by Ujjwal Shelke
def check_number(number):
    """
    Determines if a given number is positive, negative, or zero.

    Args:
        number (float or int): The input number.

    Returns:
        str: A string indicating whether the number is positive, negative, or zero.
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage:
user_input = float(input("Enter a number: "))
result = check_number(user_input)
print(f"The given number is {result}.")
