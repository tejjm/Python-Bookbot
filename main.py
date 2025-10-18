# python
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    split_text = text.split()
    num_words = len(split_text)
    print(f"Found {num_words} total words")

main()