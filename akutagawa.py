#!/usr/bin/env python3
from bs4 import BeautifulSoup
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
        ful_url = href.replace("..","https://www.aozora.gr.jp")
        print(name.rstrip() + ",", ful_url)