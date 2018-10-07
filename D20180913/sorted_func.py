'''
sorted(iter [,reverse=True, key=func])
将传入的对象按照指定的func做排序，默认为升序，指定reverse=True后为降序
key=func指定排序规则函数，不指定则按默认的字符串ascii码顺序排序
排序后返回一个新的对象，传入的对象本身不变
'''

l1 = [1, 9, 3, 7, 5, 4, 6, 2]
l2 = sorted(l1)

print(l1,"\n",l2)

l3 = ["a23","d346","h5","b1111"]
l4 = sorted(l3, reverse=True)

print(l4)

# 指定按照字符串的长度来排序，使用内置len函数
l5 = sorted(l3, key=len)
print(l5)

# 自定义排序规则，按照字符串的第二位大小来排序, 那么就需要一个取得字符串第二位值的函数
def getSecond(s):

    return s[1]

l6 = sorted(l3, key=getSecond)
print(l6)
