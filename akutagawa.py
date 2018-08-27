#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request as req

# 対象HTML
url = "http://www.aozora.gr.jp/index_pages/person879.html"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")


# 作品リスト取得処理
shoseki_list = soup.select("ol > li")
for sakuhin in shoseki_list:
    a = sakuhin.a
    if a != None:
        name = a.string
        href = a.attrs["href"]
        print(name +","+ urljoin(url, href))
