#Executed By : Ujjwal Shelke 84158
def number_to_words(number):
    # Define a dictionary to map digits to their word representations
    digit_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    # Convert the number to a string
    number_str = str(number)

    # Initialize an empty string to store the result
    result = ""

    # Iterate through each digit in the number
    for digit in number_str:
        # Get the word representation of the digit
        word = digit_words.get(digit, "")
        result += word + " "

    # Remove the trailing space
    result = result.strip()

    return result

# Example usage
user_number = int(input("Enter a number: "))
result_words = number_to_words(user_number)
print(f"The number {user_number} in words is: {result_words}")
