import re


def abbreviate(words):
    words = re.sub(r'[-_]', ' ', words).split()
    return ''.join(w[0].upper() for w in words)
