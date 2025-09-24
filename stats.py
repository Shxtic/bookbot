# Turns books_contents into single words as a list
def count_words(contents):
    counter = 0
    book_words = contents.split()
    for i in range(0, len(book_words)):
        counter += 1
    return counter


#
def count_characters(txt):
    num_characters = {}
    txt = txt.lower()
    for character in txt:
        if character in num_characters:
            num_characters[f"{character}"] += 1
        else:
            num_characters[f"{character}"] = 1

    return num_characters


#

def sort_on(items):
    return items["num"]


def sort_num_characters(num_characters):
    list_of_chars = []
    full_dict = num_characters


    for char in full_dict:
        dicts = {}

        dicts["char"] = char
        dicts["num"] = full_dict[char]
        list_of_chars.append(dicts)

    list_of_chars.sort(reverse=True, key=sort_on)

    return list_of_chars
