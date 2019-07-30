import time

# 获取时间戳
t1 = time.time()
print(t1)

# 获取当前时间的utc 时间元组
t2 = time.gmtime()
print(t2)

# 将时间戳转为utc时间元组
t3 = time.gmtime(1535356594.714616)
print(t3)

# 将时间戳转换为本地时间元组 ，本地时区 +8
t4 = time.localtime(1535356594.714616)
print(t4)

# 将时间元组转换为时间戳
t5 = time.mktime(t4)
print(t5)

# 将时间元组转换成日期时间字符串，不带参数表示获取当前时间
t6 = time.asctime(t4)
print(t6)

# 将时间戳转换为日期时间字符串
t7 = time.ctime(t1)
print(t7)

# 将一个时间元组转换成指定格式的日期时间字符串，如果时间元组不指定，则获取当前时间
t8 = time.strftime("%Y%m%d %H%M%S")
print("t8:"+t8)

# 将给定的日期时间格式字符串转换为 时间元组
t9 = time.strptime(t8, "%Y%m%d %H%M%S")
print("t9:", t9)

# print(time.ctime())

# 睡眠N秒
# time.sleep(3)

# print(time.ctime())

t10 = time.perf_counter()
print(t10)
sum = 0
for i in range(100000000):
   sum += i


t11 = time.perf_counter()
print(t11)
