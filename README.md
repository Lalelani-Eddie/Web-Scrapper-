# Web Scraper

## Overview
This Python web scraper extracts data from websites by parsing HTML content. It uses the `requests` library to fetch web pages and `BeautifulSoup` to navigate and extract specific information from the HTML structure.

## Features
- Fetches HTML content of a given webpage.
- Extracts all anchor tags (`<a>` elements) with their titles and hyperlinks.
- Saves the extracted data to a CSV file for further analysis.

## Requirements
To run this project, ensure you have the following installed:
- Python 3.6 or higher
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas` (optional, for saving data to CSV)

You can install the required libraries using the following command:
```bash
pip install requests beautifulsoup4 pandas
```

## How to Use

### 1. Clone or Download the Repository
Clone the repository or download the script to your local machine.

### 2. Update the Target URL
In the script, update the `url` variable with the website URL you want to scrape:
```python
url = "https://example.com"  # Replace with your target website
```

### 3. Run the Script
Execute the script using Python:
```bash
python DataSaver.py
```

### 4. View the Output
The script will:
1. Print extracted titles and links to the console.
2. Save the data to a file named `scraped_data.csv` in the same directory as the script.

## Code Structure
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a GET request
url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 3: Extract data
    data = []
    for item in soup.find_all('a', href=True):
        title = item.text.strip()
        link = item['href']
        data.append({"Title": title, "Link": link})
    
    # Step 4: Save to CSV
    df = pd.DataFrame(data)
    df.to_csv('scraped_data.csv', index=False)
    print("Data saved to scraped_data.csv")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
```

## Error Handling
- **Invalid URL**: Ensure the URL is correct and accessible.
- **HTTP Errors**: The script checks the HTTP status code and exits if the page cannot be retrieved.
- **Blocked Requests**: If the website blocks the request, use headers to mimic a browser request:
  ```python
  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
  }
  response = requests.get(url, headers=headers)
  ```

## Next Steps
- Extend functionality to scrape dynamic content using `selenium`.
- Add support for scraping other elements like images or tables.
- Implement error logging for better debugging.

## License
This project is open-source and available under the MIT License.

## Contact
For questions or feedback, feel free to reach out:
- **Name**: Lalelani Eddie Nene
- **Email**: [lalelaninene@gmail.com]
- **GitHub**: [https://github.com/Lalelani-Eddie]

