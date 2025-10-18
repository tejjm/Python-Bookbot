# python

from stats import get_num_words

def main():
    path = "books/frankenstein.txt"
    num_words = get_num_words(path)
    print(f"Found {num_words} total words")

main()