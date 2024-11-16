import string
import sys

# give name of text file in the books folder at execution
text_name = sys.argv[1]

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

def get_word_count(content):
    words = content.split()
    return len(words)

def main():
    with open(f'books/{text_name}.txt') as f:
        content = f.read()
        word_count = get_word_count(content)
        char_count = get_char_count(content)
        print(f"Report on {text_name}:")
        print(f"{word_count} words in this piece of text.\n")
        for letter in char_count:
            print(f"The {letter} character was found {char_count[letter]} times.")
        print("\nEnd report.")

main()