from bs4 import BeautifulSoup
import requests
import json
import re
import time
import random

class video_api:
    
    def vt(bvid):
        url=f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
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
        api=json.loads(data)
        api_dict=dict(api)
        if api_dict.get("code")==0:
            code=0
        elif api_dict.get("code")==-400:
            code=-400
        return code

    def video_stat(bvid):
        url=f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
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
        api=json.loads(data)
        api_dict=dict(api)
        video_stat=(api_dict.get("data")).get("stat")
        return video_stat




    
        

class user_api:
    
##    def user_info(uid):
##        url=f"https://api.bilibili.com/x/space/acc/info?mid={uid}"
##        head={
##            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
##            "Referer":url,
##            "Sec-Fetch-Dest":"empty",
##            "Sec-Fetch-Mode":"cors",
##            "Sec-Fetch-Site":"same-site",
##            "Pragma":"no-cache",
##            "Origin": "https://space.bilibili.com",
##            "Accept": "application/json, text/plain, */*",
##            "Accept-Encoding": "gzip, deflate, br",
##            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
##            }
##        data=requests.get(url,headers=head).text
##        api=json.loads(data)
##        api_dict=dict(api)
##        
##        while api_dict.get("code")==-799:
##            data=requests.get(url,headers=head).text
##            api=json.loads(data)
##            api_dict=dict(api)
##            print(api_dict.get("code"))
##            print(api_dict)
##            time.sleep(random.randint(1,5))
##
##        if api_dict.get("code")==0:
##            name=(api_dict.get("data")).get(name)
##        elif api_dict.get("code")==-400:
##            name="用户不存在"
    def code_check(uid):
        url=f"https://api.bilibili.com/x/relation/stat?vmid={uid}"
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
        api=json.loads(data)
        api_dict=dict(api)
        if api_dict.get("code")==0:
            code=0
        elif api_dict.get("code")==-400:
            code=-400
        return code

    def sub(uid):
        url=f"https://api.bilibili.com/x/relation/stat?vmid={uid}"
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
        api=json.loads(data)
        api_dict=dict(api)
        sub=(api_dict.get("data")).get("follower")
        return sub

##    def upstat():
##        url=f"https://api.bilibili.com/x/space/upstat?mid=2251463"
##        head={
##            "Origin":"https://space.bilibili.com",
##            "Pragma":"no-cache",
##            "Referer":url,
##            "Sec-Fetch-Dest":"empty",
##            "Sec-Fetch-Mode":"cors",
##            "Sec-Fetch-Site":"same-site",
##            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
##
##        }
##        data=requests.get(url,headers=head).text
##        print(data)
##        api=json.loads(data)
##        api_dict=dict(api)        
##        upstat=api_dict.get("data")
##        return upstat
        

        
        


            
        


        

    


        

        




        
