# US Largest Companies Web Scraper Demo

A simple, demo Python web scraper that extracts tabular data of the largest companies in the United States by revenue from Wikipedia and saves it as a CSV file.

## 🚀 Features
- Scrapes live data from the Wikipedia page "List of largest companies in the United States by revenue".
- Parses HTML structures using `BeautifulSoup`.
- Formats and organizes data efficiently using `pandas` DataFrames.
- Exports the scraped data to a clean, ready-to-use `largest_companies.csv` file.
- Includes a custom `User-Agent` header to respect the Wikimedia Foundation's bot and scraping policies.

## 🛠 Prerequisites

Make sure you have Python 3.x installed on your machine. You will also need to install the required third-party Python libraries.

You can install the dependencies using `pip`:

```bash
pip3 install requests beautifulsoup pandas
```

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-directory>
   ```

2. **Run the scraping script:**
   Execute the python script from your terminal:
   ```bash
   python web-scraping.py
   ```

3. **Check the Output:**
   Once the script finishes execution, you will see a preview of the scraped data printed in your terminal. Additionally, a new file named `largest_companies.csv` will be generated in the same directory containing the full dataset.

## 📂 Project Structure

- `web-scraping.py`: The main Python script containing the step-by-step web scraping logic.
- `largest_companies.csv`: The output file generated after successfully running the script (ignored in `.gitignore` ideally).
- `README.md`: This project documentation.

## ⚠️ Disclaimer

This project was created purely for **demo and educational purposes** to demonstrate fundamental web scraping techniques in Python. Always review and respect the `robots.txt` and Terms of Service of any website before scraping.
