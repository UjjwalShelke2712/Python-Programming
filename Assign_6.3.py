# C1-84158-Ujjwal

def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence = set(sentence.lower())
    return alphabet.issubset(sentence)


sentence = "The quick brown fox jumps over the lazy dog."
print(is_pangram(sentence))

sentence = "The quick brown fox jumped over the lazy dog."
print(is_pangram(sentence))
