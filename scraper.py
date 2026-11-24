import requests
from bs4 import BeautifulSoup
import csv
import time

url = "http://quotes.toscrape.com/page/2/"

print(f"Connecting to {url}...")

response = requests.get(url)

if response.status_code == 200:
    print("Successfully connected! Parsing data...")

    soup = BeautifulSoup(response.text,'html.parser')

    quotes = soup.find_all('div', class_='quote')

    print(f"Found {len(quotes)} quotes. Extracting text and authors...\n")

    scraped_data = []
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()

        print(f"Quote: {text}")
        print(f"Author: {author}\n")

        scraped_data.append([text, author])

        time.sleep(1)

    print("Saving data to quotes.csv...")
    with open('quotes.csv', 'w', newline="", encoding='utf-8') as file:
              writer = csv.writer(file)
              writer.writerow(['Quote', 'Author'])
              writer.writerows(scraped_data)

    print("Data successfully saved!")
else:
    print(f"Failed to connect. Status code: {response.status_code}")


