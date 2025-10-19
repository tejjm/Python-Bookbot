# python

from stats import get_num_words,count_char,sorted_list

def main():
    print("============ BOOKBOT ============")
    path = "books/frankenstein.txt"
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = get_num_words(path)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    word_count = count_char(path)
    sorted_list(word_count)
    print("============= END ===============")

main()