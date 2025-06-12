from stats import count_str_words, count_str_chars, sort_a_dict
import sys
import os

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        if not os.path.exists(book_path):
            print(f"Unable to locate book: {book_path}\n")
            sys.exit(1)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        
        book_contents = get_book_text(book_path)
        num_words = count_str_words(book_contents)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")   
        num_chars = count_str_chars(book_contents)
        list_of_sorted_dicts = sort_a_dict(num_chars)
        for d in list_of_sorted_dicts:
            if d["char"].isalpha():
                print(f"{d["char"]}: {d["count"]}")
    else:
        print("Missing required path to book text.\nUsage: python3 main.py <path_to_book>\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

