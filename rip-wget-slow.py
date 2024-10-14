import os
import subprocess
import sys
from bs4 import BeautifulSoup


def rip_website(url, output_dir):
    print(f"Ripping website: {url}")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    # Use wget to recursively download the website
    subprocess.run(['wget.exe', '--recursive',  url, '--no-parent', url], cwd=output_dir)


def extract_text_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Define CSS selectors for elements to exclude
        exclude_selectors = ['script', 'style', 'nav', '.sidebar', '#footer']  # Example selectors to exclude
        # Remove elements matching the specified selectors
        for selector in exclude_selectors:
            for tag in soup.select(selector):
                tag.extract()
        # Extract text from the HTML file
        text = soup.get_text()
        return text


def remove_excessive_blank_lines(text):
    lines = text.split('\n')
    cleaned_lines = [line for line in lines if line.strip()]
    return '\n'.join(cleaned_lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python rip-wget-slow.py <website_url>")
        return
    website_url = sys.argv[1]  # URL of the website passed as command-line argument
    output_dir = "website_dl"  # Output directory for downloaded files
    output_file = 'outputz.txt'  # Output file for extracted text

    print(f"Processing website: {website_url}")

    # Rip the website
    rip_website(website_url, output_dir)


    print("Website ripping complete")

    # Process the downloaded files
    html_files = []
    # Iterate through directories and find HTML files
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    # Extract text from HTML files and append to output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for html_file in html_files:
            text = extract_text_from_html(html_file)
            cleaned_text = remove_excessive_blank_lines(text)
            outfile.write(cleaned_text + '\n')


if __name__ == "__main__":
    main()
