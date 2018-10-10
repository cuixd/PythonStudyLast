import urllib.request
import json
import ssl

def ajaxRequest(url):

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) "
             "Chrome/23.0.1271.64 Safari/537.11"}
    req = urllib.request.Request(url, headers=headers)

    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req,context=context)

    return response.read().decode("utf8")


url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"

with open("/Users/cuixiaodong/PycharmProjects/PythonStudy/25.网络爬虫urllib模块三/douban.json","a") as f:
    for i in range(1, 11):
        # print(i)
        url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=" \
              "&start=" + str(i - 1)+ "&limit=20"
        jsonstr = ajaxRequest(url)
        f.write(jsonstr)
        f.write("\n")
        print(jsonstr)


