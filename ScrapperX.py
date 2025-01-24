import argparse
import requests
import bs4
from time import sleep
from datetime import datetime

"""
ScrapperX
Author: @Swiftglitxh
Version: 0.1
Description: A simple web scraping tool that fetches web content, extracts links, and performs directory brute-forcing.
"""

# Argument parser setup
parser = argparse.ArgumentParser(
    prog='WebScraper',
    description='A simple web scraping tool',
    epilog='Example usage: python script.py -u http://example.com'
)

current_time = datetime.now().strftime('%H:%M:%S')
version = "0.1"

parser.add_argument('-u', '--url', dest="web", type=str, required=True, help="Target website URL")
parser.add_argument('-v', '--verbose', dest="verbose", action='store_true', help="Enable verbose output")
parser.add_argument('-D', '--dirb', dest="dirb", help="Enable directory brute-forcing")
parser.add_argument('-L', '--links', dest="href",action="store_true", help="Enable directory href scrapping")

args = parser.parse_args()

# ASCII Banner
def banner():
    print("""
 ,---.                                                    ,--.   ,--.
'   .-'  ,---.,--.--. ,--,--. ,---.  ,---.  ,---. ,--.--.  \\  `.'  / 
`.  `-. | .--'|  .--'' ,-.  || .-. || .-. || .-. :|  .--'   .'    \\   
.-'    |\\ `--.|  |   \\ '-'  || '-' '| '-' '\\   --.|  |.--. /  .'.  \\ 
`-----'  `---'`--'    `--`--'|  |-' |  |-'  `----'`--''--''--'   '--'  v 0.1
                             `--'   `--'""")

# Define a fake user-agent
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

if args.dirb:
	dirb_enabled = "True"
else:
	dirb_enabled = "False"

if args.href:
	list_enabled = "True"
else:
	list_enabled = "False"

def main():
    website = args.web

    try:
        response = requests.get(website, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise an HTTP error for bad responses (404, 500, etc.)
        url_status_code = response.status_code
        encoding = response.encoding

        banner()
        print("-" * 70)
        sleep(0.2)
        print("+" + "-" * 35 + "+")
        print(f" [+] Target: {website}")
        sleep(0.2)
        print(f" [+] Status Code: {url_status_code}")
        sleep(0.2)
        print(f" [+] User-Agent: {HEADERS['User-Agent']}")
        sleep(0.2)
        print(f" [+] Encoding: {encoding}")
        sleep(0.2)
        print(f" [+] Dirb Scrapping: {dirb_enabled}")
        sleep(0.2)
        print(f" [+] Link Scrapping: {list_enabled}")
        sleep(0.2)
        print(f" [+] Author: @Swiftglitxh")
        sleep(0.2)
        print(f" [+] Version: {version}")
        print("+" + "-" * 35 + "+")

        # BeautifulSoup Parsing
        soup = bs4.BeautifulSoup(response.text, "lxml")
        sleep(0.2)
        print("╔═[+] Scraping Source Code ")
        sleep(0.2)

        # Print source code with a delay for each line
        with open("source_code.html","w")as f:
        	f.write(str(soup))
        print(f"╚═[+] [info] {current_time} source_code.html has been written.\n")


        print("═" * 120 + "\n" + "═" * 120)

        # Function to scan and print links
        def link_scan():
            print("\n ╔═ Scraping for links...")
            sleep(0.1)
            links = soup.find_all('a')
            if not links:
                print(" ╠═ [-] No links found on the page.")
                return
            
            for link in links:
                href = link.get('href')
                if href:
                    print(f" ╠═ [+] [info] {current_time} {href}")
                else:
                    print(f" ╠═ [!] [info] {current_time} No href attribute found.")
                sleep(0.01)  # Pause between links to simulate scanning

            print(f" ╚═ [X] Link Scan Complete at {current_time}")

        # Call the link scanning function
        if args.href:
        	link_scan()

        	print("\n", "═" * 75)

        # Function to scan directories from a wordlist file
        def dir_scanner():
            full_url = f"{args.web.rstrip('/')}"  # Remove trailing slash if present
            directory = "default.txt"  # The wordlist file to scan
            i = 0  # Initialize counter outside the loop

            try:
                with open(directory, "r") as f:
                    print("\n ╔═ Directory scanning started...")
                    sleep(0.01)
                    for line in f:
                        dir_path = line.strip()
                        if dir_path:  # Avoid empty lines
                            test_url = f"{full_url}/{dir_path}"
                            try:
                                response = requests.get(test_url, headers=HEADERS, timeout=5)
                                if response.status_code == 200:
                                    print(f" ╠═ [info] {current_time} [FOUND] {test_url} (200 OK)")
                                    i += 1
                                elif args.verbose:
                                    print(f" ╠═ [info] {current_time} [NOT FOUND] {test_url} ({response.status_code})")
                                sleep(0.1)  # To avoid flooding the server
                            except requests.exceptions.RequestException:
                                print(f" ╠═ [info] {current_time} [ERROR] Unable to reach {test_url}")
                                sleep(0.1)
                    if i == 0:
                        print(f" ╠═ [info] {current_time} NO directories found.")
                print(" ╠═ Directory scan complete.")
                print(f" ╚═[+] Directory's Found: {i}")
            except FileNotFoundError:
                print(f"[-] Error: The file '{directory}' was not found.")
            except Exception as e:
                print(f"[-] Error reading the file: {e}")

        # Call directory scanner if enabled by -D flag
        if args.dirb:
            dir_scanner()

    except requests.exceptions.MissingSchema:
        print("[-] Invalid URL. Make sure it includes http:// or https://")
    except requests.exceptions.HTTPError as http_err:
        print(f"[-] HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("[-] Failed to connect. Check your internet connection or the URL.")
    except requests.exceptions.Timeout:
        print("[-] Request timed out. The server took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching the URL: {e}")

if __name__ == "__main__":
    main()
