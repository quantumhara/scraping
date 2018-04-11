# run with python3
# usage: python3 ex05.py keyword
import sys
import urllib.request as req
import urllib.parse as parse
import os

#if len(sys.argv) <= 1:
#    print("usage: compile with keyword\nhyakunin.py (keyword)")
#    sys.exit()
#
#keyword = sys.argv[1]

print ("usage: compile with keyword\nEnter keyword")
keyword = input()

if len(keyword) < 1:
    print("usage: compile with keyword")
    sys.exit()

API = "http://api.aoikujira.com/hyakunin/get.php"

query = {
    "fmt": "ini",
    "key": keyword
}

params = parse.urlencode(query)
url = API + "?" + params

print ("url=", url)

with req.urlopen(url) as r :
    b = r.read()
    data = b.decode('utf-8')
    print(data)
