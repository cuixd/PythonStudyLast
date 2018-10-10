set1 = {1,2,3}

# 添加元素
set1.add("cuixd")

print(set1)

set2 = {1,2,3,(1,2,3)}

# 列表等可变对象无法作为一个独立对象添加到set，update方法将传入的对象切分后添加
# 到set中
set2 .update([1,2,3,3,4,5,5])
print(set2)

l1 = list(set2)
print(l1)

# 将列表转换成set，再转换成列表，用以去重
list1 = [1,2,3,3,4,5,5]
set3 = set(list1)
print(list(set3))


set3.remove(5)
set3.update("cuixd")
print(set3)



