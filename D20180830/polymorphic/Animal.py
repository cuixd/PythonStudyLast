
# 定义动物类，具备name属性与eat方法
class Animal:

    def __init__(self,name):

        self.name = name

    def eat(self,food):

        print(self.name + " eat " + food)

