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

# get user input for file path of websites list
file_path = input("Enter the file with proxy links: ")

# read in the websites from the file
with open(file_path, "r") as f:
    websites = [line.strip() for line in f.readlines()]

# create regex pattern to match IP addresses and ports
proxy_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+"

# function to scrape proxies from a single website
def scrape_proxies(website):
    proxies = set()
    try:
        # make request to website
        response = requests.get(website, timeout=10)
        # find all matches of proxy pattern in response text
        proxies.update(set(re.findall(proxy_pattern, response.text)))
    except:
        pass
    return proxies

# create an empty file to store scraped proxies
output_file = "scraped-proxies/scraped.txt"
os.makedirs(os.path.dirname(output_file), exist_ok=True)
open(output_file, "w").close()

# use thread pool executor to scrape proxies from all websites concurrently
with ThreadPoolExecutor(max_workers=16) as executor:
    futures = [executor.submit(scrape_proxies, website) for website in websites]
    # use tqdm to show progress bar and completion time
    for _ in tqdm(range(len(futures))):
        proxies = futures[_].result()
        # write all scraped proxies to output file in format ip:port
        with open(output_file, "a") as f:
            for proxy in proxies:
                f.write(proxy + "\n")

# remove any duplicate proxies
with open(output_file, "r") as f:
    unique_proxies = set(f.readlines())

# write all unique scraped proxies to output file
with open(output_file, "w") as f:
    f.writelines(unique_proxies)

print(colored(pyfiglet.figlet_format('\nScraping complete! All unique proxies have been saved to = scraped-proxies folder',  font='term'), 'green'))