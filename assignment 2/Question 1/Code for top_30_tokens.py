from transformers import AutoTokenizer
from collections import Counter
import re
from tqdm.auto import tqdm 

def count_unique_tokens(file_path, model_name, chunk_size=512, stride=256, top_n=30):
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    token_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        with tqdm(total=file_size(file_path), desc="Tokenizing") as pbar:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break

                tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(chunk, add_special_tokens=False)))
                token_counts.update(tokens)
                pbar.update(len(chunk))

    return token_counts.most_common(top_n)

def file_size(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file.seek(0, 2)
        return file.tell()

def main():
    input_txt_file = "C:\\Python\\new folder\\Assignment 2\\text.txt"
    model_name = 'bert-base-uncased'
    top_tokens = count_unique_tokens(input_txt_file, model_name)

    print(f'Top 30 unique tokens and their counts:')
    for token, count in top_tokens:
        print(f'{token}: {count}')

if __name__ == "__main__":
    main()
