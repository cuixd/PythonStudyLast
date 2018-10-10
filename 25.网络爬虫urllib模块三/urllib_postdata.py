import urllib.request
import urllib.parse

'''
urllib 发送post请求数据
向表单响应页发起数据请求，并以字典类型定义实际页面中响应页要接受的表单属性
对字典数据进行打包后加入请求体，打开页面返回数据
'''

# 表单响应页
url = "http://10.211.55.53:8080/test/form.html"

# 字典类型定义表单提交的数据，key的名称要与表单页的文本框name属性值一致
data = {"username": "cuixd", "passwd": "oracle"}

# 打包数据
postdata = urllib.parse.urlencode(data).encode("utf-8")

# 创建请求，加入post数据
req = urllib.request.Request(url, postdata)

response = urllib.request.urlopen(req)

print(response.read().decode("utf-8"))