import string
import sys
from stats import get_num_words, get_char_count

# give name of text file in the books folder at execution
text_name = sys.argv[1]

def main():
    with open(f'books/{text_name}.txt') as f:
        content = f.read()
        word_count = get_num_words(content)
        char_count = get_char_count(content)
        print(f"Report on {text_name}:")
        print(f"{word_count} words in this piece of text.\n")
        for letter in char_count:
            print(f"The {letter} character was found {char_count[letter]} times.")
        print("\nEnd report.")

main()
