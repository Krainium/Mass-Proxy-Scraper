import re
import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import pyfiglet
from termcolor import colored
from  datetime import datetime

now = datetime.now()

dt_string = now.strftime("%m/%d/%Y %I:%M:%S %p")

print(colored(pyfiglet.figlet_format('SCRIPT MADE BY KRAINIUM\n\nMASS PROXY-SCRAPER\n\nVERSION 1.0\n\nSCRAPES ALL PROXIES FROM A FILE WITH PROXY LINKS', font='term'), 'green'))

print(colored(pyfiglet.figlet_format(f'Date and Time: {dt_string}', font='term'), 'blue'))


file_path = input("Enter the file with proxy links: ")


with open(file_path, "r") as f:
    websites = [line.strip() for line in f.readlines()]


proxy_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+"


def scrape_proxies(website):
    proxies = set()
    try:
        
        response = requests.get(website, timeout=10)
        
        proxies.update(set(re.findall(proxy_pattern, response.text)))
    except:
        pass
    return proxies


output_file = "scraped-proxies/scraped.txt"
os.makedirs(os.path.dirname(output_file), exist_ok=True)
open(output_file, "w").close()


with ThreadPoolExecutor(max_workers=16) as executor:
    futures = [executor.submit(scrape_proxies, website) for website in websites]
    
    for _ in tqdm(range(len(futures))):
        proxies = futures[_].result()
        
        with open(output_file, "a") as f:
            for proxy in proxies:
                f.write(proxy + "\n")


with open(output_file, "r") as f:
    unique_proxies = set(f.readlines())


with open(output_file, "w") as f:
    f.writelines(unique_proxies)

print(colored(pyfiglet.figlet_format('\nScraping complete! All unique proxies have been saved to = scraped-proxies folder',  font='term'), 'green'))
