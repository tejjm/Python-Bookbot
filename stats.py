def get_num_words(file_path):
    with open(file_path) as f:
        text = f.read()
    split_text = text.split()
    num_words = len(split_text)
    return num_words

def count_char(file_path):
    with open(file_path) as f:
        text = f.read()
    words = text.split()
    lower_case = [word.lower() for word in words]
    # one_word = ""
    one_word = ''.join(word for word in lower_case)
    char_count = {}
    count = 0
    for char in one_word:
        if char not in char_count:
            count = 1
            char_count[char] = count
            count = 0
        elif char in char_count:
            count = char_count[char]+1
            char_count[char] = count
    return char_count

def sort_on(items):
    return items["num"]
def sorted_list(dictionary):
    list = []
    list = [{"char":key,"num":value} for key,value in dictionary.items()]
    list.sort(reverse=True,key=sort_on)
    for dict in list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")