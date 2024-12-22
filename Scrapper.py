import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Step 1: Send a GET request to the website
url = "https://ww1.goojara.to/eOevmp"  # Replace with your target website
response = requests.get(url, headers=headers)

# Step 2: Check the response status
if response.status_code == 200:
    # Step 3: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 4: Extract data (e.g., titles and links)
    for item in soup.find_all('a', href=True):  # Modify the tag ('a') and attributes if needed
        title = item.text.strip()  # Extract the text
        link = item['href']       # Extract the link
        print(f"Title: {title}, Link: {link}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

import pandas as pd

data = []  # List to store the scraped data
for item in soup.find_all('a', href=True):
    title = item.text.strip()
    link = item['href']
    data.append({"Title": title, "Link": link})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('scraped_data.csv', index=False)
print("Data saved to scraped_data.csv")
