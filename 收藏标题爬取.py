import time
import requests
import re
import json
import pandas as pd

num = 1
cookies = {
    "buvid4": "8DE86F88-30FC-D1A4-27D2-BF88267E398966862-022121620-Am315Z0S4rpEKgx9os3ZMA%3D%3D",
    "buvid3": "BE2C7BFC-2AFC-8984-F9A8-45218E831C4866898infoc",
    "b_nut": "1671192166",
    "_uuid": "F32E2847-AB4B-C27F-5276-995431022B9D567404infoc",
    "i-wanna-go-back": "-1",
    "rpdid": "|(J|)Jlklul~0J'uY~uk|J)~|",
    "nostalgia_conf": "-1",
    "b_ut": "5",
    "hit-dyn-v2": "1",
    "buvid_fp_plain": "undefined",
    "LIVE_BUVID": "AUTO8716744899638099",
    "is-2022-channel": "1",
    "header_theme_version": "CLOSE",
    "CURRENT_BLACKGAP": "0",
    "hit-new-style-dyn": "1",
    "CURRENT_PID": "00185d10-cd5e-11ed-9df4-331b246c567d",
    "FEED_LIVE_VERSION": "V_NO_BANNER_3",
    "CURRENT_FNVAL": "4048",
    "CURRENT_QUALITY": "80",
    "bp_video_offset_363653602": "850032460932579456",
    "SESSDATA": "a465e29d%2C1712306529%2Ca425f%2Aa1CjCjZRjvnO2NEoavABZI7sTC8-DfgVpfDmgL_djOB2q2BF1iP9bX9DciqdQWv3FF10USVi05MklybjB0TnFuOXZOUzBnRS16YmdDc0E1d2pqbVFOSmhoM25NNDlRY0h4SUk0N1V0d0dpQmEyV3NTMUtLcHM5N3VqekpZdjlGZ01vNXlETWdFQ3pnIIEC",
    "bili_jct": "f8429286185d3b22f353eb338a412d6f",
    "DedeUserID": "32347153",
    "DedeUserID__ckMd5": "6e20d89c04c0aaaa",
    "home_feed_column": "5",
    "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTcwODk4MjIsImlhdCI6MTY5NjgzMDU2MiwicGx0IjotMX0.UulgaJZQ6-vEKAsd2c7lytiToTJVoJ04dUI4ybvJ-ug",
    "bili_ticket_expires": "1697089762",
    "sid": "4ok3q5gl",
    "PVID": "1",
    "fingerprint": "eabda4545dc792438868f4b139423fb3",
    "buvid_fp": "eabda4545dc792438868f4b139423fb3",
    "b_lsid": "B3AFF977_18B189AA919",
    "innersign": "0",
    "browser_resolution": "1918-937",
    "bp_video_offset_32347153": "850768558440841251"
}
headers = {
        'Referer': 'https://www.bilibili.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }


def history_title_get():
    """
    爬取历史记录并保存为csv文件
    :return: None
    """
    oid = "661652965"
    view_at = "1696779723"
    tilte_data = []
    for i in range(61):
        print(f"上面的{oid}")
        url = f"https://api.bilibili.com/x/web-interface/history/cursor?max={oid}&view_at={view_at}&business=archive"
        json_data = json.loads(requests.get(url=url,headers=headers,cookies=cookies).text)
        all_jsondata = json_data["data"]["list"]
        for a in all_jsondata:
            print([a["title"],a["tag_name"],a["kid"],a["view_at"]])
            tilte_data.append([a["title"],a["tag_name"],a["kid"],a["history"]["bvid"]])
            oid = a["kid"]
            view_at = a["view_at"]
        print(oid)
        time.sleep(0.5)
    df = pd.DataFrame(tilte_data,columns=["tilte","tag_name","kid","bvid"])
    df.to_csv("./刘思洲的历史记录.csv")


def favlist_title_get():
    tilte_data = []
    for i in range(11):
        url = f"https://api.bilibili.com/x/v3/fav/resource/list?media_id=87591453&pn={i}&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web"
        jsondata = json.loads(requests.get(url=url,headers=headers,cookies=cookies).text)
        alldata = jsondata["data"]["medias"]
        for i in alldata:
            tilte_data.append([i["title"],i["intro"]])
            print(i["title"],i["intro"])
    df = pd.DataFrame(tilte_data,columns=["tilte","intro"])
    df.to_csv("./白姐的收藏夹2.csv")


def vedio_intro_get():
    page_content = requests.get("https://www.bilibili.com/video/BV1Bh4y1Y7hh/",headers=headers,cookies=cookies).text

    obj = re.compile(r'<li>.*?<div class="basic-desc-info">.*?<span class="desc-info-text"data-v-1d530b8d>(?P<intro>.*?)'
                     r'</span>', re.S)
    resule = obj.finditer(page_content)
    for a in resule:
        a.group("intro")
        print(a.group("intro"))


if __name__ ==  "__main__":

    history_title_get()