import re

'''
re模块
python正则表达式模块
'''

'''
match(pattern, str, flags=xx)
从目标串的开始位置进行模式匹配，成功则返回一个re匹配对象，否则返回None
flags=xxx 指定模式的一些特殊规则，比如忽略大小写、跳过某些特殊字符等等
flags有以下常用值：
re.I    忽略大小写
re.M    进行多行匹配，影响行首^匹配与$行尾匹配
re.S    使匹配识别换行符，即忽略换行符\n的特殊含义
re.U    根据unicode字符集解析字符串
re.X    更灵活的格式理解正则表达式模式

'''
# flags=re.I忽略大小写
res = re.match("www", "wwW.baidu.com", flags=re.I)
print(res)
print(res.span())

# 开始位置不能成功匹配模式，返回None
res = re.match("www", "1wwW.baidu.com", flags=re.I)
print(res)
#print(res.span())

'''
search方法与match方法类似，但是search不限定从开始必须匹配，只要目标串中能成功匹配，
则返回第一次匹配的对象和位置
'''
res = re.search("www", "1wwW.baidu.comwww", flags=re.I)
print(res)
print(res.span())

'''
findall方法，找出目标串中匹配模式的所有子串
'''
res = re.findall("www", "1wwW.baidu.comwww", flags=re.I)
print(res)
