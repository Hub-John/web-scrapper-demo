import requests
from bs4 import BeautifulSoup
import pandas as pd

# -------------------------------------------------------------
# Step 1 - Target URL
# -------------------------------------------------------------
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
print(f"\n{url}")

# -------------------------------------------------------------
# Step 2 - User-Agent - respect the Wikimedia Foundation Policy
# -------------------------------------------------------------
headers = {
    "User-Agent": "USCompanyDataScraper/1.0 (https://example.com; bot_contact@example.com)"
}

# -------------------------------------------------------------
# Step 3 - Fetch the webpage content
# -------------------------------------------------------------
response = requests.get(url, headers=headers)

# -------------------------------------------------------------
# Step 4 - Parse the HTML using BeautifulSoup
# -------------------------------------------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------------------------------------------
# Step 5 - Find the first table on the page
# Wikipedia tables usually have the class 'wikitable'
# -------------------------------------------------------------
table = soup.find("table", {"class": "wikitable"})

# -------------------------------------------------------------
# Step 6 - Extract the rows from the table
# -------------------------------------------------------------
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

# -------------------------------------------------------------
# Step 7 - Created dataframe
# -------------------------------------------------------------
df = pd.DataFrame(columns = world_table_titles)

# -------------------------------------------------------------
# Step 7 - Loop through rows (skip the header row at index 0)
# -------------------------------------------------------------
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

# -------------------------------------------------------------
# Step 8 - Shows data on terminal/command line
# -------------------------------------------------------------
print(f"\n{df}")

# -------------------------------------------------------------
# Step 9 - Convert DataFrame into CSV file
# -------------------------------------------------------------
df.to_csv("largest_companies.csv", index=False)
print("\nlargest_companies.csv file created successfully! \n")