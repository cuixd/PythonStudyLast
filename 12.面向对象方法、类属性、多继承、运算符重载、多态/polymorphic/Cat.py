from polymorphic.Animal import Animal


# 定义Cat类，继承自Animal
class Cat(Animal):

    def __init__(self, name):

        super(Cat,self).__init__(name)


