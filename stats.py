def get_num_words(file_path):
    with open(file_path) as f:
        text = f.read()
    split_text = text.split()
    num_words = len(split_text)
    return num_words

def count_char(file_path):
    char_count = {}
    with open(file_path) as f:
        for ch in f.read().lower():
            if "a" <= ch <= "z":
                char_count[ch] = char_count.get(ch,0)+1


    #     text = f.read()
    # text = text.lower()
    # new_text = ""
    # for char in text:
    #     if "a" <= char <= "z":
    #         new_text+=char
    # for char in new_text:
    #     if char not in char_count:
    #         count = 1
    #         char_count[char] = count
    #         count = 0
    #     elif char in char_count:
    #         count = char_count[char]+1
    #         char_count[char] = count
    return char_count


def sort_on(items):
    return items["num"]
def sorted_list(dictionary):
    list = []
    list = [{"char":key,"num":value} for key,value in dictionary.items()]
    list.sort(key=lambda x: x["num"], reverse=True)
    for dict in list:
        if "a" <= dict["char"] <= "z":
            print(f"{dict['char']}: {dict['num']}")
