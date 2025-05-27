from stats import get_num_words, get_num_chars, get_sorted_list_of_dicts
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    if (len(sys.argv) < 2):
        print("Please provide book path by running: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = sys.argv[1]
    book = get_book_text(book_filepath)
    num_words = get_num_words(book)
    num_chars = get_num_chars(book)

    print(f"============ BOOKBOT ============\n\
Analyzing book found at {book_filepath}...\n\
----------- Word Count ----------\n\
Found {num_words} total words\n\
--------- Character Count -------")

    char_list = get_sorted_list_of_dicts( get_num_chars(book) )
    for char in char_list:
        if not char["char"].isalpha():
            continue
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()