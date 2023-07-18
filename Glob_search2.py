import glob
import os.path
import re


def search_words_in_text_files(words, formats):
    file_list = glob.glob('search/*')  # Get a list of all files in the 'search' directory
    if not file_list:
        print("No files found.")
        return

    found_files = []
    for file_name in file_list:
        if not any(file_name.endswith(ext) for ext in formats):
            continue

        with open(file_name, 'r', encoding='utf-8') as text_file:
            lines = text_file.readlines()
            found_words = []
            for word in words:
                word_occurrences = []
                for line_num, line in enumerate(lines, start=1):
                    occurrences = [(m.start(), m.end()) for m in re.finditer(word, line)]
                    if occurrences:
                        word_occurrences.append((line_num, occurrences))
                if word_occurrences:
                    found_words.append((word, word_occurrences))
            if found_words:
                found_files.append((file_name, found_words))

    if not found_files:
        print("No files containing the word(s) found.")
    else:
        print("Files containing the word(s):")
        for file_name, found_words in found_files:
            print(f"File: {file_name}")
            for word, word_occurrences in found_words:
                print(f" - Word: {word}")
                for line_num, occurrences in word_occurrences:
                    print(f"   - Line: {line_num}")
                    for start, end in occurrences:
                        print(f"     - Location: {start}-{end}")


search_words_in_text_files(['CMD', 'example'], ['.txt', '.docx'])
