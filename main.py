from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import smtplib

# evn path and variables
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

SMTP_ADDRESS=os.getenv('SMTP_ADDRESS')
SENDER=os.getenv("SENDER")
PASSWORD=os.getenv("PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Accept-Language": "pt-PT,pt;q=0.9,en-GB;q=0.8,en;q=0.7,es-ES;q=0.6,es;q=0.5,en-US;q=0.4,fr;q=0.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",

    
}

URL="https://www.amazon.es/-/pt/dp/B0B1YJRL9X/ref=sr_1_1?crid=2KC9ENME9RCD3&keywords=garmin+enduro+2&qid=1678548009&s=electronics&sprefix=garmin+enduro+%2Celectronics%2C97&sr=1-1"

response = requests.get(url=URL, headers=headers)

website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

# print(soup.prettify())

# Get Price
article_price = soup.find(name="span", class_="a-offscreen").getText().split(",")[0]

price_1 = article_price.split()[0]
price_2 = article_price.split()[1]

price = int(price_1+price_2)

title = soup.find(name="span", id="productTitle").getText().split("Relógio")[0]

# Define Price Targuet
BUY_PRICE = 2000

#Send Email
if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(SENDER, PASSWORD)
        connection.sendmail(
            SENDER,
            SENDER,
            f"Subject: Amazon Price Alert!\n{message}"
            )