import string
import sys

def get_char_count(content):
    # alphabatize dictionary first for later output
    char_count = {}
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        char_count[letter] = 0
    content = content.lower()
    for letter in content:
        if letter in char_count.keys():
            char_count[letter] += 1
    return char_count

def get_num_words(content):
    words = content.split()
    return len(words)