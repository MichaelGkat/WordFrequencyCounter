# main.py
from word_frequency import count_frequency

def main():
    filename = input("Enter the name of the text file (e.g., 'example.txt'): ")

    ignore_case_input = input("Do you want to ignore case when counting words? (yes/no): ").strip().lower()
    ignore_case = ignore_case_input == "yes"

    save_file_input = input("Do you want to save the results to a file? (yes/no): ").strip().lower()
    if save_file_input == "yes":
        output_filename = input("Enter the output file name (e.g., 'word_frequencies.txt'): ")
        file_format = input("Choose output format (text/csv): ").strip().lower()
        while file_format not in ["text", "csv"]:
            print("Invalid format. Please choose either 'text' or 'csv'.")
            file_format = input("Choose output format (text/csv): ").strip().lower()
    else:
        output_filename = None
        file_format = None

    count_frequency(filename, ignore_case=ignore_case, 
                         output_filename=output_filename, file_format=file_format)

if __name__ == "__main__":
    main()
