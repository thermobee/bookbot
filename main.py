from stats import count_words
from stats import count_characters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    characters = count_characters(book)
    final_count = count_words(book)
    
    print("{0} words found in the document".format(final_count))
    print(characters)

main()