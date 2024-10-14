import os
import json
import argparse
from bs4 import BeautifulSoup

def extract_text_from_paragraphs(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        paragraphs = soup.find_all('p')
        text = '\n'.join(paragraph.get_text() for paragraph in paragraphs)
        h1_text = soup.find('h1')
        h1_text = h1_text.get_text().strip() if h1_text else "No Title Found"
        return text, h1_text

def remove_excessive_blank_lines(text):
    lines = text.split('\n')
    cleaned_lines = [line for line in lines if line.strip()]
    return '\n'.join(cleaned_lines)

def main(input_directory, output_file):
    html_files = []
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for html_file in html_files:
            text, h1_text = extract_text_from_paragraphs(html_file)
            cleaned_text = remove_excessive_blank_lines(text)
            json_record = {
                "title": h1_text,
                "text": cleaned_text
            }
            json_line = json.dumps(json_record, ensure_ascii=False)
            outfile.write(json_line + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract the useful text from HTML files recursively within a directory and save as JSONL.")
    parser.add_argument("input_directory", type=str, help="Directory containing HTML files to process")
    parser.add_argument("output_file", type=str, help="Output JSONL file name")
    args = parser.parse_args()
    main(args.input_directory, args.output_file)