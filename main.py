from stats import count_words, count_chars
from report import print_report
import sys


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    return ''

def print_usage():
    print(f"Usage: python3 main.py <path_to_book>")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    filepath: str = sys.argv[1]
    content = get_book_text(filepath)
    num_words = count_words(content)
    chars_count = count_chars(content)
    print_report(filepath, num_words, chars_count)
    return 0


if __name__ == '__main__':
    main()
