from file_read import read_file
from word_counter import clean_text, count_words, sort_word_count

import csv

def save_to_text_file(word_count, output_filename="word_frequencies.txt"):
    with open(output_filename, "w") as file:
        for word, count in word_count:
            file.write(f"{word}: {count}\n")
    print(f"Word frequencies saved to {output_filename}")

def save_to_csv_file(word_count, output_filename="word_frequencies.csv"):
    with open(output_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Frequency"])  # Header 
        for word, count in word_count:
            writer.writerow([word, count])
    print(f"Word frequencies saved to {output_filename}")

    

def count_frequency(filename : str, ignore_case = True, output_filename=None, file_format='txt'):
    text = read_file(filename)

    if text:

        cleaned_text = clean_text(text)

        word_count = count_words(cleaned_text)

        sorted_word_count = sort_word_count(word_count)

        for word, count in sorted_word_count:
            print(f"{word}: {count}")

        if output_filename:
            if file_format == "csv":
                save_to_csv_file(sorted_word_count, output_filename)
            else:
                save_to_text_file(sorted_word_count, output_filename)