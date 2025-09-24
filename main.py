from stats import count_words
from stats import count_characters
from stats import sort_num_characters
import sys

def get_book_text(file):
    with open(file) as f:
        book_str = f.read()
    return book_str



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: pass
# Path to book
    book_path = sys.argv[1]
# getting books entire contents
    book_contents = get_book_text(book_path)

    num_of_words = count_words(book_contents)

    print(f"Found {num_of_words} total words")

    num_of_characters =count_characters(book_contents)
    list_of_sorted_dict = sort_num_characters(num_of_characters)

#Print Output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for i in range(0,len(list_of_sorted_dict)):
        char = ""
        numb = int

        dict_cache = list_of_sorted_dict[i]
        numb = dict_cache["num"]
        char = dict_cache["char"]
        if char.isalpha() == True:
            print(f"{char}: {numb}")
        else: pass
    print("============= END ===============")




main()
