from file_read import read_file
from word_counter import clean_text, count_words, sort_word_count

def count_frequency(filename : str):
    text = read_file(filename)

    if text:

        cleaned_text = clean_text(text)

        word_count = count_words(cleaned_text)

        sorted_word_count = sort_word_count(word_count)

        for word, count in sorted_word_count:
            print(f"{word}: {count}")