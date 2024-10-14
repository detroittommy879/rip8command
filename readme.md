# Python Tools for ripping full websites recursively to .jsonl file  

Can be used to create a Open AI Assistant / Custom Chatbot from a blog or other site. Still working on figuring out the best way(s) to grab the
useful text. rip-wget-slow.py to rip a website then rip8command.py or rip8progressbar.py to process it into a jsonl file.


## Getting Started

Create a new virtualenv and do:
pip install beautifulsoup4 tqdm

## How to use

Rip a website to local folder:

python rip-wget-slow.py <websiteurl>

Still experimenting, it uses wget to recursively download an entire website / blog but has some filtering that is unneeded.

------------

python rip8command.py downloaded_website example.jsonl

usage: rip8command.py [-h] input_directory output_file

Extract the useful text from HTML files recursively within a directory and save as JSONL.

positional arguments:
  input_directory  Directory containing HTML files to process
  output_file      Output JSONL file name

This file can be fed into an AI to create a chatbot that knows about that data.
