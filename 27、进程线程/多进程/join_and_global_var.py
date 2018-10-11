from multiprocessing import Process
from time import sleep
import datetime

# 定义一个全局的变量
num = 100

def run():

    # 子进程方法中引入全局num, 相当于copy了一个num, 是独立的 相当于内部定义了 num = 100
    global num

    # 子进程中执行num + 1
    num += 1
    print(num)
    print("子进程开始", datetime.datetime.now())
    sleep(15)
    print("子进程结束", datetime.datetime.now())

'''
主进程和子进程默认情况下，运行是各自独立的，子进程的运行过程并不依赖主进程的状态，
同样，主进程的执行状态也不关心子进程的执行状态，因此以下这段代码的表现是：
主进程开始后很快结束，而子进程在开始运行后由于需要等待三秒，后结束
'''

'''
if __name__ == "__main__":

    print("主进程开始")

    p = Process(target=run)
    p.start()

    print("主进程结束")
'''

'''
join方法，使子进程加入到主进程的运行过程中来，
表现为，主进程在执行到join方法时，需要等待子进程执行结束才继续完成主进程
'''

if __name__ == "__main__":

    print("主进程开始",datetime.datetime.now())

    p = Process(target=run)
    p.start()
    sleep(5)
    print("主进程在运行",datetime.datetime.now())
    p.join()
    sleep(5)

    # 主进程的num依然为100，不受其他线程的影响，多个进程间无法共用全局变量
    print(num)
    print("主进程结束",datetime.datetime.now())