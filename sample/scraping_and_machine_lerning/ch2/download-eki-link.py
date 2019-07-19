from urllib.parse import *
from urllib.request import *
from bs4 import BeautifulSoup
import os, os.path, time, pathlib

path = str(pathlib.Path(__file__).resolve().parent)
html = open(path + "/src/eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a[href]")
result = []
for a in links:
    href = a.attrs["href"]
    title = a.string
    result.append((title, href))

savepath = "./out";
if not os.path.exists(savepath): os.mkdir(savepath)
for title, url in result:
    path = savepath + "/" + url + ".html"

    a_url = urljoin("http://example.com", url)
    print("download=" + a_url)

    #urlretrieve(a_url, path)

    time.sleep(1)