# 以*号开头的参数，表示该参数是一个不定个数的参数，类型是一个元组tuple
def getSum(*num):
    sum = 0
    for n in num:
        sum += n
    print(type(num))
    return sum

sum = getSum(1,2,3,4)
print(sum)

# 以两个*号开头的参数，也是不定个数参数，但是它的类型是一个字典，赋值时必须以
# 键值对的形式赋予
def dictParam(**dict):
    print(dict)
    print(type(dict))

dictParam(x = 1, y = 2)

# lambda表达式格式  lamdba args1, xargs2, ...xrgsN : body
# 以lambda 开始，以冒号分隔参数列表与运算表达式
sum = lambda  x, y : x + y
print(sum(1,2))