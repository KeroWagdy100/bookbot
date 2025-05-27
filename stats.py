def get_num_words(txt: str) -> int:
    return len( txt.split() )

def get_num_chars(txt: str) -> dict[str, int] | None:
    map = {}
    for c in txt:
        c = c.lower()
        if (c in map):
            map[c] += 1
        else:
            map[c] = 1
    return map