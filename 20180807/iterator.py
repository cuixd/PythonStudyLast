# python 迭代器

list1 = [1,3,5,"cui"]
i1 = iter(list1)
item = next(i1)
print(item)
item = next(i1)
print(item)
item = next(i1)
print(item)
item = next(i1)
print(item)


# 使用迭代器接收多行用户输入

endstr = "end"
str1 = ""

for  line in iter(input, endstr):
    str1 +=  line + "\n"

print(str1)