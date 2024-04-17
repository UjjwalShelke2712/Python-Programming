#Code By Ujjwal Shelke
def filter_long_words(word_list, length):
    """
    Filters words longer than a given length from a list of words.

    Args:
        word_list (list): A list of words.
        length (int): The minimum length for filtering.

    Returns:
        list: A list of words longer than the specified length.
    """
    return [word for word in word_list if len(word) > length]

# Example usage:
words = ["Pankaj", "Jitendra", "Yugal", "Devendra", "Ujjwal"]
min_length = 5
filtered_words = filter_long_words(words, min_length)
print(f"Words longer than {min_length} characters: {filtered_words}")
