from multiprocessing import Process, Queue
import time, os

'''
进程间数据通信
前面讲到全局变量在各个子进程间是无法共用的，为此 multiprocessing模块提供了Queue队列类
各个进程间通过引用同一个队列来实现数据共享
'''

# 写进程，向一个队列写数据
def write(q):
    print("写进程启动  ", os.getpid())
    for c in ["A", "B", "C", "D"]:
        q.put(c)

    print("写进程结束")

# 读进程，循环读取队列中的数据
def read(q):
    print("读进程启动  ", os.getpid())
    while True:
        c = q.get(True)
        print(c)


if __name__ == "__main__":

    print("主进程开始")
    q = Queue()

    wp = Process(target=write, args=(q,))
    rp = Process(target=read, args=(q,))

    wp.start()
    rp.start()

    wp.join()

    # 读进程中是死循环，通过以下方式结束
    rp.terminate()

    print("主进程结束")