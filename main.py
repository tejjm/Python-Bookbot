# python

from stats import get_num_words,count_char

def main():
    path = "books/frankenstein.txt"
    num_words = get_num_words(path)
    print(f"Found {num_words} total words")
    word_count = count_char(path)
    print(word_count)

main()