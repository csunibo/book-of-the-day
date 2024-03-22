import os
from os.path import basename

import requests
from bs4 import BeautifulSoup

IMG_FOLDER = os.getenv("IMG_FOLDER", "img")

if not os.path.exists(IMG_FOLDER):
    os.mkdir(IMG_FOLDER)

url = "https://boyter.org/2016/04/collection-orly-book-covers/"
urlPrefix = "https://boyter.org"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
# imgs = soup.findAll('img')
imgs = list(map(lambda x: urlPrefix + x["src"], soup.findAll("img")))
for lnk in imgs:
    with open(os.path.join("img", basename(lnk)), "wb") as f:
        f.write(requests.get(lnk).content)
print(imgs)
