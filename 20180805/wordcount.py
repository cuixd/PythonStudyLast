# 用字典的方式统计字符串中单词出现的次数
str = 'cuixd is a good boy cuixd is a nice man cuixd is a hehe man'
wlist = str.split(" ")
wcount = {}

for v in wlist:
    if wcount.get(v) == None:
        wcount[v] = 1
    else:
        wcount[v] += 1

print(wcount)
print(wcount["cuixd"])

key = "cuixd"

cuixdcount = {"cuixd":0}

for v in wlist:
    if "cuixd" == v:
        cuixdcount["cuixd"] += 1

print(cuixdcount)
