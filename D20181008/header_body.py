import urllib.request
import ssl
import random

# 模拟浏览器，添加请求头的user-agent浏览器客户端属性
# 这一步是针对mac sarfai浏览器的特殊处理，创建ssl非安全验证体
ssl._create_default_https_context = ssl._create_unverified_context

url = "http://wwww.baidu.com"

# 完整的请求头是一个字典类型，包含很多属性，这里只指定User-Agent用来模拟浏览器
headers = { "User-Agent":
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}
req = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(req)

data = response.readlines()
for line in data:
    print(line.decode("utf8"))

# 实际使用中，只使用一种浏览器的user-agent在进行网页爬取时，会被网站检测为爬虫从而封杀IP，所以需要指定多个，随机
# 选取一个来模拟，避免被有效监测
agentlist = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) "
             "Chrome/23.0.1271.64 Safari/537.11",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 "
             "(KHTML, like Gecko) Version/10.1.1 Safari/603.2.4",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 "
             "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
             "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 "
             "Ubuntu/10.10 (maverick) Firefox/3.6.10"]

# random模块的选择函数，从list中随机选取一个元素
agentstr = random.choice(agentlist)

# 这次的请求体不指定headers，因为我们获取的是一个字符串，而headers需要的是一个字典
req = urllib.request.Request(url)

# 通过请求体的以下方法来添加header
req.add_header("User-Agent", agentstr)


response = urllib.request.urlopen(req)
print(response.read().decode("utf8"))