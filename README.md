<img width="1894" height="951" alt="image" src="https://github.com/user-attachments/assets/438e2f11-2d5e-48c6-9e1b-44a52ca310f5" />


**Author:** @Swiftglitxh  
**Version:** 0.2  
**Category:** Web Reconnaissance  
**License:** MIT  

ScrapperX is a lightweight web reconnaissance tool designed to fetch web content, extract links, and perform directory brute‑forcing with optional verbose output. It is built for learning, testing, and **authorized** security assessments.

---

## Overview

ScrapperX automates common reconnaissance tasks used during the early stages of web analysis. It retrieves and parses HTML content, identifies hyperlinks, saves page source locally, and brute‑forces directories using a supplied wordlist. Output is color‑coded for clarity and quick analysis.

---

## Features

- Fetch and parse target web page content
- Extract all discovered hyperlinks
- Save full HTML source code to a local file
- Directory brute‑forcing using a wordlist
- Multi‑threaded directory scanning
- Verbose mode for detailed status output
- Colored terminal output (Colorama)

---

## Installation

### 1. Clone the Repository
```
git clone https://github.com/swiftglitxh/scrapperx.git
cd scrapperx
```
2. Install Dependencies
```pip install -r requirements.txt```
Usage
```Basic Scan
python scrapperx.py -u http://example.com
```
Enable Link Scraping
```python scrapperx.py -u http://example.com -L```
Directory Brute‑Forcing
```python scrapperx.py -u http://example.com -D wordlist.txt```
Verbose Mode
```python scrapperx.py -u http://example.com -D wordlist.txt -V```
Set Custom Thread Count
```python scrapperx.py -u http://example.com -D wordlist.txt -T 20```
Example Output
```
==========================================================
 ScrapperX v0.2 | Author: @Swiftglitxh
============================================================
[+] Target: https://example.com
[+] Status Code: 200
[+] User-Agent: Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/118.0
[+] Encoding: UTF-8
[+] Threads: 15
[+] Dirb Enabled: default.txt
[+] Link Scraping: False
[+] Version: 0.2
[+] Author: @Swiftglitxh
------------------------------------------------------------
 [+] 21:30:12 source_code.html written

 [+] Scraped Links
 [1] http://example.com/about
 [2] http://example.com/contact

 [+] Directory scan started
 [O][200] http://example.com/admin
 [O][200] http://example.com/account
 [O][200] http://example.com/admin
 [X][404] http://example.com/gitlow

 [+] Directory scan complete | Found: 3
```
⚠️ **Requirements** ⚠️ 

> Python 3.x

> argparse

> requests

> beautifulsoup4

> colorama

**Project Structure**
```
scrapperx/
│
├── scrapperx.py
├── default.txt
├── requirements.txt
└── README.md
```

--
**Legal Disclaimer**
> ScrapperX is intended for educational purposes and authorized testing only.
> 
> Do NOT use this tool against systems you do not own or have explicit permission to test.

The author @Swiftglitxh assumes no responsibility for misuse or damage caused by this tool.
