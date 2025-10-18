def get_num_words(file_path):
    with open(file_path) as f:
        text = f.read()
    split_text = text.split()
    num_words = len(split_text)
    return num_words