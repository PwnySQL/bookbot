def print_report(filepath: str, num_words: int, chars_count: dict):
    char_count_list = sorted([{"char": k, "num": v} for k,v in chars_count.items()], key=lambda el: el["num"], reverse=True)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    print("\n".join(map(lambda el: "{char}: {num}".format(**el), filter(lambda el: el["char"].isalpha(), char_count_list))))
