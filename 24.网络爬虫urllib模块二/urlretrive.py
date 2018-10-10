import urllib.request

# 直接将读取到的内容写入到文件
urllib.request.urlretrieve("http://www.baidu.com",
                           filename="/Users/cuixiaodong/PycharmProjects/PythonStudy/24.网络爬虫urllib模块二/baidu.html")

# 清理内容缓存，当程序迟迟不能结束时，最好手动释放缓存
urllib.request.urlcleanup()
