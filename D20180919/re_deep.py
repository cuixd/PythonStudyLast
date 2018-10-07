import re

str1 = 'cuixd    is  a good man'

'''
字符串切割
'''

# 使用字符串自带的split方法，指定空格切割，当空格的数量有多个时，切割后获得的结果会有空格元素
l = str1.split(" ")
print(l)

# 使用正则re模块的切割方法，指定模式分隔符，则完美解决上述问题
# 指定多个空格 " +"
l2 = re.split(" +", str1)
print(l2)


'''
re.finditer(pattern, string[, flags=])
类似findall对目标字符串进行模式匹配查找，但是将结果返回为一个迭代器，
以防止结果过大，直接占用过多内存
'''
str2 = "I am cuixd, I'm from China, cuixd is a good man! cuixd is a nice man"
it1 = re.finditer("cuixd is.*?man", str2)
while True:
    try:
        print(next(it1))
    except StopIteration as e:
        break


'''
字符串的替换与修改
re.sub(pattern, repl, string[, count=, flags=])
re.subn(pattern, repl, string[, count=, flags=])

pattern 匹配的模式
repl 用来替换匹配的新子串
string 源串
count 匹配替换多少个

sub 返回类型为字符串
subn 返回类型为元组，元组的第一个元素为替换后的新串，第二个元素是匹配的个数
'''

str3 = re.sub("cuixd", "llj", str2)
print(str3)
print(type(str3))

tup1 = re.subn("(cuixd)", "llj", str2)
print(tup1)
print(type(tup1))


'''
使用() 对匹配模式进行分组，提取分组子串, 每一对括号表示一个组
'''
str4 = "0571-85667341"
m = re.match("((\d{4})-(\d{8}))", str4)

# 编号为0的组固定为源串，也就是str4
print(m.group(0))

# 后面的编号依次为各个括号指定的分组，分组从外到内，从左到右进行编号
print(m.group(1))
print(m.group(2))
print(m.group(3))


print("###############我是分割线####################")


# 为每个分组指定分组名称 格式 ?P<name>
# 演示，实际生产中应避免使用中文
m1 = re.match("(?P<完整>(?P<区号>\d{4})-(?P<电话>\d{8}))", str4)

# 通过指定分组名称来获取指定分组
print(m1.group("完整"))
print(m1.group("区号"))
print(m1.group("电话"))

'''
编译正则表达式为对象
以上所做的正则匹配，当需要用同一个模式去匹配不同字符串时，需要重复的将正则模式写多遍
编译就是将正则表达式编译为一个对象，方便重复调用
'''

re_str = '(?P<完整>(?P<区号>\d{4}|\d{3})-(?P<电话>\d{8}))'
# 将正则表达式编译为对象
re_part = re.compile(re_str)

# 通过正则对象的方法来匹配不同的串
# 原先由re模块调用的如match search findall finditer split等方法都改由正则对象调用
m2 = re_part.match("0571-85667341")
print(m2.group("完整"))
print(m2.group("区号"))
print(m2.group("电话"))

m3 = re_part.match("010-12345678")
print(m3.group("完整"))
print(m3.group("区号"))
print(m3.group("电话"))

