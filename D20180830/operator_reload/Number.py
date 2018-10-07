

# 定义一个类，演示运算符重载
class Number:

    def __init__(self, num):

        self.num = num

    # python内部提供了一系列运算符对应的内部方法，比如+法运算符对应的就是__add__方法
    # 重写+法运算符对应的__add__方法，将对象中的num属性执行乘法运算后构建一个新的Number类实例返回
    def __add__(self, other):

        return Number(self.num * other.num)

    '''
    def __add__(self, other):

        return self.num * other.num
    '''

    def __str__(self):

        return "Number.num:" + str(self.num)



n1 = Number(2)
n2 = Number(4)

# 执行对象相加
n3 = n1 + n2

# 产生一个新的Number对象
print(n3)
print(type(n3))