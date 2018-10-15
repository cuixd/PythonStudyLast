from multiprocessing import Process
import os

'''
多进程类Process的自定义封装
'''

class CuixdProcess(Process):

    def __init__(self, name):

        super().__init__()
        self.name = name

    # 重写Process类的run方法，实现自定义功能
    def run(self):

        print("%s进程启动，进程id:%d" % (self.name, os.getpid()))

        print("%s进程停止，进程id:%d" % (self.name, os.getpid()))


if __name__ == "__main__":

    p = CuixdProcess("王者荣耀")

    # 进程启动后会自动调用run方法
    p.start()
    p.join()
    print("主进程正在运行,进程id:%d" %(os.getpid()))