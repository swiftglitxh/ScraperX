# ScraperX
![image](https://github.com/user-attachments/assets/553b76e3-9101-4195-8f82-22a8a7f74a4e)


**Author:** @Swiftglitxh  
**Version:** 0.1  
**Description:**  
A simple web scraping tool that fetches web content, extracts links, and performs directory brute-forcing.

## Features

- Fetch and parse web page content.
- Extract all available links from the target website.
- Save the page source code to a file.
- Perform directory brute-forcing using a wordlist.
- Verbose mode for detailed output.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/swiftglitxh/webscraper.git
   cd webscraper
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python webscraper.py -u http://example.com
```

### Enable Verbose Output

```bash
python webscraper.py -u http://example.com -v
```

### Perform Directory Brute-Forcing

```bash
python webscraper.py -u http://example.com -D wordlist.txt
```

## Example Output

```
--------------------------------------------------------------
 [+] Target: http://example.com
 [+] Status Code: 200
 [+] User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
 [+] Encoding: UTF-8
 [+] Dirb Scrapping: True
 [+] Link Scrapping: True
 [+] Author: @Swiftglitxh
 [+] Version: 0.1
--------------------------------------------------------------
═ Scraping Source Code ═
╔═ Scraping for links...
╠═ [+] http://example.com/contact
╠═ [+] http://example.com/about
╚═ [X] Link Scan Complete at 12:30:45
```

## Requirements

- Python 3.x
- Modules: `argparse`, `requests`, `bs4`, `datetime`

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---
