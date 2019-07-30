

class Person(object):

    # 类属性，定义在类体中的属性，可通过类名直接访问
    country = "China"

    def __init__(self, name, age, country):

        # 实例属性，定义在构造方法中的self.属性，只能通过实例名访问
        self.name = name
        self.age = age

        # 定义了一个与类属性同名的实例属性
        self.country = country

    def getCountry(self):

        return self.country


p1 = Person("cuixd",33,"中国")

# 通过对象访问到的country是对象实例属性
print(p1.getCountry())
print(p1.country)

# 通过类名访问的country是类属性
print(Person.country)

# 通过实例访问的同名属性，优先为实例属性，当实例无此属性，才会访问类属性
# 为避免代码混乱和导致混淆，应避免类属性与实例属性重名

print("-------优先级测试------------")


print("实例属性删除前:" + p1.country)

# python动态语言，可以动态删除或添加实例属性
del p1.country

# 删除实例属性country后，通过实例变量访问到的就是类属性country了
print("实例属性删除后:" + p1.country)

# 重新添加实例的country属性，并改变其值
p1.country = "家里蹲"
print("实例属性重新添加后:" + p1.country)

# 类属性也可以动态修改
Person.country = "china"
print(Person.country)
