# News Scraper (`news_scapper.py`)

A simple Python script to scrape headlines from a news website and save them to a text file.

## Features

- Fetches the homepage of a website (default: [Indian Express](https://indianexpress.com))
- Extracts headlines (assumed to be inside `<h2>` tags)
- Saves headlines into `headlines.txt` in UTF-8 encoding

## Requirements

- Python 3.x
- requests library
- beautifulsoup4 library

Install dependencies using:
pip install requests beautifulsoup4
