# 以*号开头的参数，表示该参数是一个不定个数的参数，类型是一个元组tuple
def getsum(*num):
    s = 0
    for n in num:
        s += n
    print(type(num))
    return s


sum1 = getsum(1, 2, 3, 4)
print(sum1)

# 以两个*号开头的参数，也是不定个数参数，但是它的类型是一个字典，赋值时必须以
# 键值对的形式赋予


def dictparam(**vdict):
    print(vdict)
    print(type(vdict))


dictparam(x=1, y=2)

# lambda表达式格式  lamdba args1, xargs2, ...xrgsN : body
# 以lambda 开始，以冒号分隔参数列表与运算表达式,原则上不建议这么使用，建议使用def来定义函数

getadd = lambda x, y: x + y
print(getadd(1, 2))
