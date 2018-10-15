import threading, os, time

'''
threading线程模块
线程与进程不同，一个进程下的所有线程共享同一份数据
'''
# 全局变量
num = 0


# 定义线程任务，循环执行加减操作
def run(n):

    global num

    # threading.current_thread().name 获取当前线程的名称
    print("%s正在运行" % threading.current_thread().name)
    for i in range(1000000):
        num = num - n
        num = num + n


if __name__ == "__main__":

    print("主线程正在运行 ", threading.current_thread().name)

    # 创建两个子线程，name属性指定线程名称
    t1 = threading.Thread(target=run, name="线程1", args=(5,))
    t2 = threading.Thread(target=run, name="线程2", args=(6,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # 获得的num值不一定为0，因为存在线程代码同步的问题，
    # 导致num的运算并不像想象的那样加减同一个数而保持不变
    print(num)
    print("主线程结束")
