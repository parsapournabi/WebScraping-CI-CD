from lxml import html
from urllib.request import getproxies as gp
import requests
import csv

# Variables
url = "https://www.tgju.org/coin"

if gp():
    response = requests.get(url, proxies={"http": gp().get("http"), "https": gp().get("http")})
else:
    response = requests.get(url)


tree = html.fromstring(response.text)
tables = tree.xpath("//table//ancestor::div//child::div[*[1]/@class = *[2]/@class and count(*) = 6]/*//table")

with open("output.csv", "w", newline="", encoding="utf-8-sig") as csv_file:
    writer = csv.writer(csv_file)
    if not tables:
        writer.writerow("Error: table is empty!")
        exit()

    for table in tables:
        for row in table.xpath(".//tr"):
            cells = row.xpath(".//th | .//td")
            row_data = [cell.text_content().strip() for cell in cells]
            writer.writerow(row_data)
        writer.writerow([])

print("Table wrote completely")
