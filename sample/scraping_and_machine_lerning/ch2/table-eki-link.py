from urllib.parse import *
from urllib.request import *
from bs4 import BeautifulSoup
import os, os.path, time, pathlib

path = str(pathlib.Path(__file__).resolve().parent)
html = open(path + "/src/eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")

table = soup.select_one("table")
tr_list = table.find_all("tr")
result = []
for tr in tr_list:
    row_data = []
    td_list = tr.find_all("td")
    for td in td_list:
        row_data.append(td.get_text())
    result.append(row_data)

for row in result:
    print(",".join(row))