from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

proc_files={}

def enum_links(html, base):
    soup-BeautifulSoup(html, "html.parser")
    links=soup.select("link[rel-'stylesheet']")
    links+=soup.select("a[href]")
    result=[]

def download_file(url):
    o=urlparse(url)
    savepath="./"+o.netloc+o.path
    if not os.path.exists(savepath):
        print("mkdir=", savepath)
        makedirs(savepath)
    try:
        print("download=", url)
        urlretrive(ur, savepath)
        time.sleep(1)
        return savepath
    except:
        print("failed download:", url)
        return None

def analize_html(url, root_url):
    savepath=download_file(url)
    if savepath is None: return
    if savepath in proc_files: return
    proc_files[savepath]=True
    print("analize_html=", url)
    html=open(savepath, "r", encoding="utf-8").read()
    links=enum=links(html, url)
    for link_url in links:
        if link_url.find(root_url) != 0: continue
        if re.serach(r".(html|htm)$", link_url):
            analize_html(link_url, root_url)
            continue
        download_file(link_url)

if __name__ == "__main__":
    url="http://docs.python.jp/3.5/library/"
    analize_html(url, url)
