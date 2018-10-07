

class Father:

    def __init__(self,surname, fname):

        self.surname = surname
        self.__fname = fname


    def makeMoney(self):

        print("挣钱养家")

    def sleep(self):

        print("呼呼大睡")

    def getFname(self):

        return self.__fname