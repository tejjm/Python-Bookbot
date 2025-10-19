# python
import sys
from stats import get_num_words,count_char,sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        print("============ BOOKBOT ============")
        # path = "books/frankenstein.txt"
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        num_words = get_num_words(path)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        word_count = count_char(path)
        sorted_list(word_count)
        print("============= END ===============")
    
main()