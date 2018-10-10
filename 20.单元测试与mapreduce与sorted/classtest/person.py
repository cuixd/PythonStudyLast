

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def getAttr(self, v):
        return self.__getattribute__(v)


if __name__ == "__main__":

    p = Person("cuixd", 33)

    print(p.getAttr("name"))