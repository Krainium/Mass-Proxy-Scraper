# 🌐 Mass Proxy Scraper

A multithreaded **Python proxy scraper** that collects large numbers of proxies from multiple proxy-list websites.

The script reads a file containing **proxy source URLs**, scrapes each website concurrently, extracts all proxies in **IP:PORT format**, removes duplicates, and saves the final list.

The tool also includes **terminal banners, colored output, and a progress bar** to make scraping easier to monitor.

---

# ✨ Features

* 🌍 Scrapes proxies from **multiple websites simultaneously**
* ⚡ Uses **ThreadPoolExecutor** for faster scraping
* 🔎 Extracts proxies using **regex pattern matching**
* 📊 **Progress bar** using `tqdm`
* 🎨 Colored terminal output
* 🖥 ASCII banners using `pyfiglet`
* 📁 Automatically creates output folders
* 🔁 **Automatically removes duplicate proxies**
* 🕒 Displays **current date and time** when the script starts

---

# 🧰 Requirements

* Python **3.7+**

### Python Modules

Built-in modules:

* `re`
* `os`
* `datetime`
* `concurrent.futures`

External modules:

* `requests`
* `tqdm`
* `pyfiglet`
* `termcolor`

---

# 📦 Installation

Clone the repository:

```id="bczlrc"
git clone https://github.com/krainium/mass-proxy-scraper.git
cd mass-proxy-scraper
```

Install required dependencies:

```id="tiqpeb"
pip install requests tqdm pyfiglet termcolor
```

Or install using a **requirements file**.

Create `requirements.txt`:

```id="2jrrs0"
requests
tqdm
pyfiglet
termcolor
```

Install dependencies:

```id="x3xt9h"
pip install -r requirements.txt
```

---

# 🚀 Usage

Run the script:

```id="tsf82o"
python proxy-scraper.py
```

You will be prompted to enter a file containing **proxy source URLs**.

Example:

```id="7nmbaz"
Enter the file with proxy links: sources.txt
```

---

# 📄 Example Proxy Sources File

Example `sources.txt`:

```id="r76m9y"
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt
https://www.proxy-list.download/api/v1/get?type=http
https://openproxy.space/list/http
```

The script will scrape all proxies from these URLs.

---

# 📂 Output

All scraped proxies will be saved to:

```id="qg1gpx"
scraped-proxies/scraped.txt
```

Example output:

```id="m1fbzw"
192.168.1.10:8080
45.76.23.19:3128
103.45.67.89:80
172.16.45.2:8080
```

Duplicates are **automatically removed**.

---

# 🖥 Example Terminal Output

```id="o6dse1"
SCRIPT MADE BY KRAINIUM

MASS PROXY-SCRAPER
VERSION 1.0

SCRAPES ALL PROXIES FROM A FILE WITH PROXY LINKS

Date and Time: 03/12/2026 08:41:12 PM

Scanning websites...
Progress: 100%

Scraping complete!
All unique proxies have been saved to = scraped-proxies folder
```

---

# 📂 Project Structure

```id="nlcz54"
mass-proxy-scraper/
│
├── proxy-scraper.py
├── sources.txt
├── requirements.txt
├── scraped-proxies/
│   └── scraped.txt
└── README.md
```

---

# ⚠️ Notes

* This tool only **scrapes publicly available proxy lists**.
* Proxy availability and speed depend on the **source websites**.
* Many proxies may be **dead or slow**.

---

# 👨‍💻 Author

Krainium
GitHub: https://github.com/krainium

---

# 📜 License

MIT License
