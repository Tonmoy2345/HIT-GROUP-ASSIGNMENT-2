import csv
from collections import Counter
import re

def get_top_words(file_path, top_n=30, chunk_size=1024):
    word_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            words = re.findall(r'\b(?![0-9]+\b)\w+\b', chunk.lower()) 
            word_counts.update(words)

    return word_counts.most_common(top_n)

def write_top_words_to_csv(top_words, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Count'])
        writer.writerows(top_words)

def main():
    input_txt_file = "C:\\Python\\new folder\\Assignment 2\\text.txt"
    output_csv_file = 'Top 30 most common words.csv'

    top_words = get_top_words(input_txt_file)
    write_top_words_to_csv(top_words, output_csv_file)

    print(f'Top 30 words and their counts saved to {output_csv_file}')

if __name__ == "__main__":
    main()
