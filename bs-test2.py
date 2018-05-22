# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><body>
  <h1 id="title">スクレイピングとは</h1>
  <p id="body">Webページを解析すること</p>
  <p>任意の箇所を抽出すること</p>
</body></html>
"""

# HTMLを解析する
soup = BeautifulSoup(html, 'html.parser')

# find() メソッドで取り出す
title = soup.find(id="title")
body = soup.find(id="body")

# テキスト部分を表示
print ("#title=" + title.string)
print ("#body=" + body.string)
