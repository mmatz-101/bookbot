def get_num_words(text: str) -> int:
    words: list[str] = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    char_dict: dict[str, int] = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_chars_dict(char_dict: dict[str, int]) -> dict[str, int]:
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
    return sorted_char_dict
