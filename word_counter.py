
import string

def clean_text(text : str) -> str:
    return text.translate(str.maketrans('', '', string.punctuation)).lower()


def count_words(text : str) -> dict:
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def sort_word_count(word_count : dict) -> list:
    return sorted(word_count.items(), key = lambda item : item[1], reverse = True)