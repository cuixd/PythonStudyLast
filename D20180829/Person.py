
# 定义一个Person类


class Person:

    # 类属性，如果无需指定类属性，可以直接在__init__方法中定义对象属性
    name = ""
    age = 0

    # 定义构造方法，在构造方法中定义成员属性并赋值
    # 当显式定义了有参数的构造方法后，就不能使用默认的空构造方法来实例化对象
    # self类似java中的this，代指当前实例，但在Python中self并不是关键字，可以用其他任何变量标识符代替，如a
    def __init__(self,name,age):
        self.name = name
        self.age = age

        # __class__ 类名变量，
        # 必要时在类中使用self.__class__("songf",31) 来实例化一个本类对象，就相当于Person("songf",31)
        print(self.__class__)

    # 类的成员方法
    def speak(self):
        print("My name is "+ self.name)

    def eat(self,food):
        print("eat "+ food)

    # 析构函数，实例销毁时被调用，比如程序结束时、手动del 对象变量名、方法内实例化的对象当方法执行结束时 都会触发析构函数
    def __del__(self):
       print("这是析构函数，在对象销毁时执行")

    # 描述实例的方法，在执行print(对象)时调用，默认的__str__方法是返回实例的内存地址，
    # 通过重写，来展示自己想要输出的内容，类似java的tostring方法
    def __str__(self):
        return "我的名字叫%s，我今年%d岁" %(self.name, self.age)
    # 与__str__方法类似，在命令行终端中执行print(对象)时被调用
    def __repr__(self):
        return "My name is %s，I am %d years old" %(self.name, self.age)


p1 = Person("cuixd",33)

print(p1)
p1.speak()
p1.eat("apple")

p2 = Person("lilj",32)
p2.speak()
p2.eat("香蕉")

# 使用默认空构造方法会报错
# p3 = Person()
print(p1)
print(p2)