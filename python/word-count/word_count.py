from collections import Counter
import re


def count_words(sentence):
    sentence = re.sub(r'[^a-zA-Z0-9\s\,_\']', '', sentence.lower())
    sentence = re.sub(r'([^n\'])\'+|\'{2}', r'\1', sentence)
    words = re.split('[\s\,\n_]+', sentence)
    words = [word for word in words if word != '']
    return dict(Counter(words))
