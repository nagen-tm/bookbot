import string

def get_char_count(content):
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
    with open('books/frankenstein.txt') as f:
        contents = f.read()
        word_count = get_word_count(contents)
        char_count = get_char_count(contents)
        print("Book report: ")
        print(f"{word_count} words in this book.")
        for letter in char_count:
            print(f"The {letter} character was found {char_count[letter]} times.")
        print("End report.")

main()