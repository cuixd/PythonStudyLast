#1、 引入整个模块
# import cuixd

# 调用模块中的函数时，需要指定模块名
#cuixd.sayGood()

#2、 引入自定义模块中的某个函数
from cuixd import saygood,sayhello

#3、引入某个模块的所有函数
#from cuixd import *

# 直接调用函数，而无需指定模块名
saygood()

s1 = "cuixd@xinguangnet.com----123456"
print(s1.index("----"))
print(s1[0:21])






