# -*- encoding:utf-8 -*-
print("%%")
# 字符串前r表示跳过字符串中的转义
print(r"\r\n\t")
result = eval("1 , 2")
print("result = ", result)
print("result的类型：", type(result))
str1 = "123456789"
print(str1[4:7])

print(len(str1))

print(str1.center(20, "#"))

del str1
str2 = "cuixd is a very very good man"
print(str2.count("very", 14, -1))

print(str2.find("very", 10, 21))
del str2

