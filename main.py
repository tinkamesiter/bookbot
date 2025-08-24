from stats import word_number
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    book_text = get_book_text(file)
    word_count = word_number(book_text)
    char_count = count_characters(book_text)
    char_list = sort_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_list:
        if char.isalpha():
            print(f"{char}: {count}")
        else:
            continue
    print("============= END ===============")

main()