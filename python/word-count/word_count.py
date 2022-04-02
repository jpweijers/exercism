import re


def count_words(sentence):
    sentence = re.sub(r'[^a-zA-Z0-9\s\,_\']', '', sentence.lower())
    sentence = re.sub(r'([^n\'])\'+|\'{2}', r'\1', sentence)
    words = re.split('[\s\,\n_]+', sentence)
    return {k: words.count(k) for k in words if k != ''}
