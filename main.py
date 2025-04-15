import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters

# Check for a second argument (path to the text)
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_location = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        return file_contents

def main():
    book = get_book_text(book_location)
    characters = count_characters(book)
    final_count = count_words(book)
    
    #Format and Print
    print("============ BOOKBOT ============")
    print("Analyzing book found at {0}...".format(book_location))
    print("----------- Word Count ----------")
    print("Found {0} total words".format(final_count))
    print("--------- Character Count -------")
    # Format the dictionary
    for k,v in sort_characters(characters):
        if k.isalpha():
            print("{0}: {1}".format(k, v))
    print("============= END ===============")
    
main()