from collections import Counter


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict:
    return Counter(text.lower())
