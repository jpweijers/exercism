LETTER_VALUES = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

LETTER_VALUES = {l: score for score, letters in LETTER_VALUES.items()
                 for l in letters}


def score(word):
    print(LETTER_VALUES)
    return sum(LETTER_VALUES[l.upper()] for l in word)
