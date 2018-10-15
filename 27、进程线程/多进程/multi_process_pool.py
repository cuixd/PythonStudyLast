import multiprocessing
import os
import time
import random


def run1(processid):
    print("子进程%d启动，进程号%d" %(processid, os.getpid()))
    time.sleep(random.choice([1,2,3]))
    print("子进程%d结束" %(processid))


if __name__ == "__main__":

    print("主进程开启")

    # 创建进程池，Pool方法可以指定参数n，表示进程池的容量，默认为CPU的核心数
    ppool = multiprocessing.Pool()

    # 循环创建5个子进程
    for i in range(1,6):
        ppool.apply_async(run1,args=(i,))

    # 必须先close, 再join
    ppool.close()
    ppool.join()

    print("主进程结束")
