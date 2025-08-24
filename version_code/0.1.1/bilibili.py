from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import re
import time
import random

url=f"https://api.bilibili.com/x/web-interface/view?bvid="
head={
    "Origin":"https://space.bilibili.com",
    "Pragma":"no-cache",
##    "Referer":url,
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-site",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
} 

class video_api:
    
    def vt(bvid):
        url=f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
        
        data=requests.get(url,headers=head).text
        api=json.loads(data)
        api_dict=dict(api)
        for find in api_dict.get("data"):
            if find=="season_id":
                video_aid=(api_dict.get("data")).get("aid")
                video_list=((((api_dict.get("data")).get("ugc_season")).get("sections"))[0]).get("episodes")
                for video in video_list:
                    now_aid=video.get("aid")
                    if now_aid==video_aid:
                        vt=((video.get("arc")).get("stat")).get("vt")
                        break
                break
            else:
                vt="未加入合集"                        
        return vt

    def code_check(bvid):
        url=f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"

        data=requests.get(url,headers=head).text
        api=json.loads(data)
        api_dict=dict(api)
        if api_dict.get("code")==0:
            code=0
        elif api_dict.get("code")==-400:
            code=-400
        return code

    def video_stat(bvid):
        url=f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"

        data=requests.get(url,headers=head).text
        api=json.loads(data)
        api_dict=dict(api)
        video_stat=(api_dict.get("data")).get("stat")
        return video_stat

    def video_owner(bvid):
        url=f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"

        data=requests.get(url,headers=head).text
        api=json.loads(data)
        api_dict=dict(api)
        video_owner=(api_dict.get("data")).get("owner")
        return video_owner   

    def video_data(bvid):
        url=f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"

        data=requests.get(url,headers=head).text
        api=json.loads(data)
        api_dict=dict(api)
        video_data=[]
        video_data.append((api_dict.get("data")).get("pic"))
        video_data.append((api_dict.get("data")).get("title"))
        video_data.append((api_dict.get("data")).get("pubdate"))
        video_data.append((api_dict.get("data")).get("ctime"))

        return video_data

    def video_face(url_video,pic_id):
        url=url_video

        data=requests.get(url,headers=head).content
        with open(f"img/{pic_id}.png",mode="wb") as f:
            f.write(data)

        return None
            

class user_api:
    
    def code_check(uid):
        url=f"https://api.bilibili.com/x/relation/stat?vmid={uid}"

        data=requests.get(url,headers=head).text
        api=json.loads(data)
        api_dict=dict(api)
        if api_dict.get("code")==0:
            code=0
        elif api_dict.get("code")==-400:
            code=-400
        return code

    def sub(uid):
        url=f"https://api.bilibili.com/x/relation/stat?vmid={uid}"

        data=requests.get(url,headers=head).text
        api=json.loads(data)
        api_dict=dict(api)
        sub=(api_dict.get("data")).get("follower")
        return sub


    def name(uid):
        url=f"https://www.bilibili.com/list/{uid}"

        data=requests.get(url,headers=head).text
        data_soup=BeautifulSoup(data,"html.parser")
        data_attrs=(data_soup.find(itemprop="author")).attrs
        name=data_attrs.get("content")
        return name

    def video_list(uid):
        url=f"https://www.bilibili.com/list/{uid}"

        video_list=[]
        data=requests.get(url,headers=head).text
        data_soup=BeautifulSoup(data,"html.parser")
        data_soup_str=str(data_soup.find(string=re.compile("window.__INITIAL_STATE__=")))
        data_soup_str_treat_0=data_soup_str.lstrip("window.__INITIAL_STATE__=")
        data_soup_str_treat=data_soup_str_treat_0[:-122]
        data_dic=json.loads(data_soup_str_treat)
        data_resourceList=list(eval(str(data_dic.get("resourceList"))))
        data_video_num=int(((data_soup.find(class_="list-count")).string)[2:])

        for video in data_resourceList:
            video_dic=eval(str(video))
            bvid=str(video_dic.get("bvid"))
            video_list.append(bvid)

        page=(((data_video_num)-20)//19)+1

        while page>0:
            page-=1
            url=f"https://www.bilibili.com/list/{uid}?bvid={str(video_list[-1])}"
            data=requests.get(url,headers=head).text
            data_soup=BeautifulSoup(data,"html.parser")
            data_soup_str=str(data_soup.find(string=re.compile("window.__INITIAL_STATE__=")))
            data_soup_str_treat_0=data_soup_str.lstrip("window.__INITIAL_STATE__=")
            data_soup_str_treat=data_soup_str_treat_0[:-122]
            data_dic=json.loads(data_soup_str_treat)
            data_resourceList=list(eval(str(data_dic.get("resourceList"))))

            video_list_new=[]

            for video in data_resourceList:
                video_dic=eval(str(video))
                bvid=str(video_dic.get("bvid"))
                video_list_new.append(bvid)
        
            video_list.extend(video_list_new[5:])
            time.sleep(0.1)

        return video_list

    def video_list_show(uid):
        url=f"https://www.bilibili.com/list/{uid}"

        video_list=[]
        data=requests.get(url,headers=head).text
        data_soup=BeautifulSoup(data,"html.parser")
        data_soup_str=str(data_soup.find(string=re.compile("window.__INITIAL_STATE__=")))
        data_soup_str_treat_0=data_soup_str.lstrip("window.__INITIAL_STATE__=")
        data_soup_str_treat=data_soup_str_treat_0[:-122]
        data_dic=json.loads(data_soup_str_treat)
        data_resourceList=list(eval(str(data_dic.get("resourceList"))))
        data_video_num=int(((data_soup.find(class_="list-count")).string)[2:])

        video_list.append(data_video_num)

        for video in data_resourceList:
            video_dic=eval(str(video))
            bvid=str(video_dic.get("bvid"))
            video_list.append(bvid)

        return video_list

    def video_list_clock(uid,year):
        url=f"https://www.bilibili.com/list/{uid}"

        
        video_list=[]
        data=requests.get(url,headers=head).text
        data_soup=BeautifulSoup(data,"html.parser")
        data_soup_str=str(data_soup.find(string=re.compile("window.__INITIAL_STATE__=")))
        data_soup_str_treat_0=data_soup_str.lstrip("window.__INITIAL_STATE__=")
        data_soup_str_treat=data_soup_str_treat_0[:-122]
        data_dic=json.loads(data_soup_str_treat)
        data_resourceList=list(eval(str(data_dic.get("resourceList"))))
        data_video_num=int(((data_soup.find(class_="list-count")).string)[2:])

        video_list_clock=[]

        for video in data_resourceList:
            video_dic=eval(str(video))
            bvid=str(video_dic.get("bvid"))
            video_list.append(bvid)
            pubdate=datetime.fromtimestamp((video_api.video_data(f"{bvid}"))[2])
            if pubdate.strftime("%Y")==f"{year}":
                video_list_clock.append(pubdate.strftime("%m"))
            else:
                return video_list_clock

        page=(((data_video_num)-20)//19)+1

        while page>0:
            page-=1
            url=f"https://www.bilibili.com/list/{uid}?bvid={str(video_list[-1])}"
            data=requests.get(url,headers=head).text
            data_soup=BeautifulSoup(data,"html.parser")
            data_soup_str=str(data_soup.find(string=re.compile("window.__INITIAL_STATE__=")))
            data_soup_str_treat_0=data_soup_str.lstrip("window.__INITIAL_STATE__=")
            data_soup_str_treat=data_soup_str_treat_0[:-122]
            data_dic=json.loads(data_soup_str_treat)
            data_resourceList=list(eval(str(data_dic.get("resourceList"))))

            for video in data_resourceList[5:]:
                video_dic=eval(str(video))
                bvid=str(video_dic.get("bvid"))
                video_list.append(bvid)
                pubdate=datetime.fromtimestamp((video_api.video_data(f"{bvid}"))[2])
                if pubdate.strftime("%Y")==f"{year}":
                    video_list_clock.append(pubdate.strftime("%m"))
                else:
                    return video_list_clock
                
            time.sleep(0.1)

        return video_list_clock
        

        
        


            
        


        

    


        

        




        
