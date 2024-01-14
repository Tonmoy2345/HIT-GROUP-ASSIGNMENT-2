import csv
import os

def extract_text_from_csv(csv_file_path):
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        text_column = [row['TEXT'] for row in reader if 'TEXT' in row]
    return text_column

def write_to_txt(output_file_path, text_list):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for text in text_list:
            file.write(text + '\n')

def extract_and_merge_csv_files(csv_folder_path, output_txt_file):
    all_text = []

    for filename in os.listdir(csv_folder_path):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(csv_folder_path, filename)
            text_column = extract_text_from_csv(csv_file_path)
            all_text.extend(text_column)

    write_to_txt(output_txt_file, all_text)
    print(f'Text extracted from CSV files and saved to {output_txt_file}')

csv_folder = "C:\\Python\\new folder\\Assignment 2"

output_txt_file = 'text.txt'

extract_and_merge_csv_files(csv_folder, output_txt_file)
