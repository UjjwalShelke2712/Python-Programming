#Executed By Ujjwal Shelke
def find_longest_word(word_list):
    """
    Finds the longest word in a given list of words.

    Args:
        word_list (list): A list of words.

    Returns:
        tuple: A tuple containing the length of the longest word and the word itself.
    """
    if not word_list:
        return 0, None

    longest_word = max(word_list, key=len)
    return len(longest_word), longest_word

# Example usage:
words = ["Ujjwal", "Umesh", "Kiran", "Rupesh", "Kaustubh"]
length, longest = find_longest_word(words)
print(f"The longest word is '{longest}' with a length of {length} characters.")
