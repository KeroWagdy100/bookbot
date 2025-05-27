from stats import get_num_words, get_num_chars

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    num_chars = get_num_chars(book)

    print(f"{num_words} words found in this document")
    print(f"{num_chars} chars found in this document")

main()