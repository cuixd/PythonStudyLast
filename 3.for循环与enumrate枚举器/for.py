# for循环
for m in [1, 3, 5, 7, 9]:
    print(m)

print("\n\n")
# enumerate迭代器，获得列表的下标和元素
for idx, m in enumerate(["cuixd", "is", "a", "good", "man"]):
    print(idx, m)

# range(n,m) 产生一个 [n...m)的连续数值列表
# 计算1到100的和
sum = 0
for num in range(1,101):
    sum += num

print(sum)

# python循环中也有break和continue，与其他程序语言的用法一致

