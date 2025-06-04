from pathlib import Path
import sys

from stats import get_chars_dict, get_num_words, sort_chars_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    book_path = Path(book)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = sort_chars_dict(chars_dict)
    print_report(book_path, num_words, sorted_chars_dict)


def get_book_text(path: Path) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path: Path, num_words: int, sorted_chars_dict) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_chars_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")


main()
