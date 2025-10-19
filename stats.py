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
    lower_case = []
    for word in words:
        l_word = word.lower()
        lower_case.append(l_word)
    one_word = ""
    for word in lower_case:
        one_word+=word
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
    # list = [{key:value} for key,value in dictionary.items()]
    for key,value in dictionary.items():
        x = {"char":key,"num":value}
        list.append(x)
    list.sort(reverse=True,key=sort_on)
    for dict in list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")