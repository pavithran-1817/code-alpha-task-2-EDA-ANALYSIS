
import requests
import csv
import re
import time
from bs4 import BeautifulSoup

all_books = []

# Website-la irukkura 50 pages-ai scrape pannuvom
for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping page {page}...")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.select("article.product_pod")

        if not books:
            print("Books not found. Stopping.")
            break

        for book in books:
            title = book.h3.a["title"]

            price_text = book.select_one(
                ".price_color"
            ).get_text(strip=True)

            price = float(
                re.sub(r"[^0-9.]", "", price_text)
            )

            rating = book.select_one(
                ".star-rating"
            )["class"][1]

            all_books.append({
                "Book Name": title,
                "Price (£)": price,
                "Rating": rating
            })

        # Website-ku requests-ku naduvula small delay
        time.sleep(0.3)

    except requests.RequestException as error:
        print(f"Page {page} error: {error}")
        break

# Ella books-ai CSV file-la save pannuvom
with open(
    "books.csv", "w", newline="", encoding="utf-8-sig"
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Book Name", "Price (£)", "Rating"]
    )
    writer.writeheader()
    writer.writerows(all_books)

print("\n--- SCRAPING COMPLETED ---")
print("Total books collected:", len(all_books))
print("CSV saved as books.csv")

if all_books:
    prices = [book["Price (£)"] for book in all_books]
    print("Highest price:", max(prices))
    print("Lowest price:", min(prices))
    print("Average price:", round(sum(prices) / len(prices), 2))
