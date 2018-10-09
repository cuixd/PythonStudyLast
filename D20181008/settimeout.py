import urllib.request

# 指定timeout 参数设置超时时间

for i in range(10):
    try:
        response = urllib.request.urlopen("http://www.baidu.com", timeout=0.05)
        print(len(response.read().decode("utf-8")))
    except:
        print("请求超时，继续下一次")