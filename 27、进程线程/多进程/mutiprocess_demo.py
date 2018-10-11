from multiprocessing import Process
from time import sleep
import os

def run(name):

    # os的getpid获取当前进程号  getppid获取父进程号
    while True:
        print("%s进程%d正在运行，父进程id：%d" %(name, os.getpid(), os.getppid()))
        sleep(1)


if __name__ == "__main__":

    '''
    Process类构造方法，创建一个进程
    target指明进程需要执行的任务，通常是一个方法
    args指定需要执行的任务的参数，如果有的话；
    args是一个元组，如果任务只有一个参数，需要在元素后加逗号,
    '''
    p = Process(target=run, args=("亡者农药",))
    p.start()

    while True:

        print("主进程%d正在运行" %(os.getpid()))
        sleep(1)
