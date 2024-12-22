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
