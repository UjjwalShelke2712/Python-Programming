#Code By Ujjwal Shelke 84158
def check_vowel_or_consonant(char):
    """
    Determines if a given character is a vowel or a consonant.

    Args:
        char (str): The input character.

    Returns:
        str: A message indicating whether the character is a vowel or a consonant.
    """
    vowels = "aeiouAEIOU"

    if char.isalpha():
        if char in vowels:
            return f"'{char}' is a vowel."
        else:
            return f"'{char}' is a consonant."
    else:
        return "Invalid input. Please enter an alphabetic character."

try:
    user_char = input("Enter a character: ")
    result = check_vowel_or_consonant(user_char)
    print(result)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
