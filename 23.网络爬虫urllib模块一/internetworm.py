import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")

'''
将网页内容保存为html文件
'''
# data = response.read()
# print(data)
#
# with open("/PycharmProjects/PythonStudy/23.网络爬虫urllib模块一/baidu.html","wb") as f:
#     f.write(data)


# 将网页内容读取为行列表，以便循环处理
data = response.readlines()

for line in data:
    print(line.decode("utf-8"))

# 响应的一些信息
print('a', response.info())

# http请求返回码
print('b', response.getcode())

# 获取本次爬取的url
print('c', response.geturl())


# 将地址栏的url复制出来后，其中的中文空格或者特殊字符等会被编码，导致无法识别
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E7%8E%8B%E8%80%85%E8%" \
      "8D%A3%E8%80%80&rsv_pq=9f4415590004e9a4&rsv_t=8b23ED%2B3s2IztpC4eGqDkaQq%2F%2FXSxrYxIFRyfWI" \
      "tUvg%2BmiQ%2F%2FJV1NkdZX%2Fw&rqlang=cn&rsv_enter=1&rsv_sug3=16&rsv_sug1=11&rsv_sug7=101"
# 将编码后的url地址进行还原，获得原样
newurl = urllib.request.unquote(url)
print('d', newurl)

