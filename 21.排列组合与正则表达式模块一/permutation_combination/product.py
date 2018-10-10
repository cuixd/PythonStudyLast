import itertools

'''
product方法，产生序列的全部排列与组合能够形成的串
'''

# 基本上只能跑到8位的  测试了10位 我的mac 16G内存完全不够，显示python进程最后占用达到了50多G，内存不足被系统kill了
# Process finished with exit code 137 (interrupted by signal 9: SIGKILL)
l1 = list(itertools.product("0123456789", repeat=5))

print(len(l1))


# 简易迭代器对象生成
iter = (x for x in range(1,11))

# print(next(iter))
# print(next(iter))
# print(next(iter))

for i in iter:

    print(i)




s = "0"

print(ascii(s))