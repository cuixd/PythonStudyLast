from functools import reduce

'''
author: cuixd
python的map和reduce内建函数，其中reduce方法需要import
map(func, iter)
map方法两个参数，第一个是一个函数，其实就是map分发需要使用的处理逻辑
第二个是一个可迭代对象，比如字符串，列表，set，字典等
map方法会使用传入的func方法来处理迭代对象的每一个元素，并将处理的结果重新返回为一个可迭代对象，必要时要将其转换为具体的类型

reduce(func1, iter1)
reduce方法同样有两个参数，
第一个参数也是一个函数名，表示reduce合并处理需要执行的逻辑
第二个参数同样是一个可迭代对象，比如字符串，列表，set，字典等
传给reduce方法的func1的参数列表必须是两个，表示要将可迭代对象的两个元素传入进行处理，再将处理得到的结果再与下一个元素进行处理，
其实就是迭代合并，最终reduce方法会返回的一个合并后的结果，如求和、求最值、统计等等
'''

# 定义一个map处理方法，返回一个传入列表的最大元素
def getMax(l):

    l.sort()
    return l[-1]


# 定义一个二维列表，每个元素是一个列表
list1 = [[1,5],[2,7],[4,10]]

# 将list1的每一个元素传入到getMax函数获取其最大值
res = map(getMax, list1)

# 将返回的可迭代对象转换为list
l1 = list(res)
print(type(l1))

print(l1)


# 定义一个reduce处理方法，比较两个元素的值，获取最大值
def getMax1(a, b):
    if a >= b:
        return a
    return b

# 将map处理得到的结果l1，传入给getMax1函数，结合reduce方法迭代获取最大值
a = reduce(getMax1, l1)

print(a)