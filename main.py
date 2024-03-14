import requests
from bs4 import BeautifulSoup
from os.path import basename
import os

os.mkdir('img')

url = "https://boyter.org/2016/04/collection-orly-book-covers/"
urlPrefix = "https://boyter.org"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
#imgs = soup.findAll('img')
imgs = list(map(lambda x: urlPrefix+x['src'], soup.findAll('img')))
for lnk in imgs:
    with open(os.path.join('img', basename(lnk)), "wb") as f:
        f.write(requests.get(lnk).content)
print(imgs)
