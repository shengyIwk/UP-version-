from bs4 import BeautifulSoup
import requests

url="https://space.bilibili.com/1254952605?spm_id_from=333.788.0.0"

head={
##    "Host": "bilibili.com",
    "Origin":"https://space.bilibili.com",
    "Pragma":"no-cache",
    "Referer":url,
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-site",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

data=requests.get(url,headers=head).text
print(data)
data_soup=BeautifulSoup(data,"html.parser")
print(data_soup)

str_data=str(data_soup)
if "1570" in str_data:
    print("1")
else:
    print("0")

import requests
 



