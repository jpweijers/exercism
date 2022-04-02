import re


def is_isogram(string):
    string = re.sub('-|\'|\s', '', string).lower()
    return len(string) == len(set(string))
