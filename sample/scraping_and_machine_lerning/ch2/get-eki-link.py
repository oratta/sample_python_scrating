from bs4 import BeautifulSoup
import os
import pathlib

os.system('pwd')

path = str(pathlib.Path(__file__).resolve().parent)
html = open(path + "/src/eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a[href]")

result = []
for a in links:
    href = a.attrs["href"]
    title = a.string
    result.append((title,href))

print(result)