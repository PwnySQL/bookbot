def get_book_text(filepath) -> str:
    with open(filepath) as f:
        return f.read()
    return ''


def main():
    content = get_book_text('./books/frankenstein.txt')
    print(content)


if __name__ == '__main__':
    main()
