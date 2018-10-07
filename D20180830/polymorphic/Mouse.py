from polymorphic.Animal import Animal


# 定义Mouse类，继承自Animal
class Mouse(Animal):

    def __init__(self, name):
        super(Mouse, self).__init__(name)
