from stats import count_words


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    return ''


def main():
    content = get_book_text('./books/frankenstein.txt')
    num_words = count_words(content)
    print(f"Found {num_words} total words")
    return 0


if __name__ == '__main__':
    main()
