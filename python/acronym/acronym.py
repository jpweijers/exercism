import re


def abbreviate(words):
    words = re.sub(r'[-_]', ' ', words)
    return ''.join(w[0].upper() for w in words.split() if w[0].isalnum())
