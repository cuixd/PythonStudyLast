import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")

'''
将网页内容保存为html文件
'''
# data = response.read()
# print(data)
#
# with open("/PycharmProjects/PythonStudy/D20181005/baidu.html","wb") as f:
#     f.write(data)


# 将网页内容读取为行列表，以便循环处理
data = response.readlines()

for line in data:
    print(line.decode("utf-8"))


