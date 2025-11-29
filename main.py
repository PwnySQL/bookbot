from stats import count_words, count_chars
from report import print_report


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    return ''


def main():
    filepath: str = './books/frankenstein.txt'
    content = get_book_text(filepath)
    num_words = count_words(content)
    chars_count = count_chars(content)
    print_report(filepath, num_words, chars_count)
    return 0


if __name__ == '__main__':
    main()
