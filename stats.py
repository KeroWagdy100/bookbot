def get_num_words(txt: str) -> int:
    return len( txt.split() )

def get_num_chars(txt: str) -> dict[str, int]:
    map = {}
    for c in txt:
        c = c.lower()
        if (c in map):
            map[c] += 1
        else:
            map[c] = 1
    return map

def sort_on(dict):
    return dict["num"]

def get_sorted_list_of_dicts(dictionary: dict[str, int]) -> list[dict]:
    sorted_dicts = []
    for char in dictionary:
        sorted_dicts.append({"char": char, "num": dictionary[char]})
    sorted_dicts.sort(key=sort_on, reverse=True)
    return sorted_dicts
