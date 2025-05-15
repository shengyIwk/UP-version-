from bs4 import BeautifulSoup
import requests


url="https://www.bilibili.com/list/1254952605"

head={
    "Origin":"https://space.bilibili.com",
    "Pragma":"no-cache",
    "Referer":url,
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-site",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}


data=requests.get(url,headers=head).text

data_soup=BeautifulSoup(data,"html.parser")

print(data_soup)
