import threading

# 定义一个线程锁，注意这个锁的定义一定是在主线程，也就是所有子线程共用的范围中定义
# 而不能在线程所要执行的方法中定义，只有所有的子线程共用这个锁，才能保证锁定代码保持同步
lock = threading.Lock()
num = 0


def run(n):
    print(threading.current_thread().name,"运行")

    # 如果将锁定义在这里，这是每个子线程各自的锁，并不能同步所有子线程代码同步，所以是错误的
    # lock = threading.Lock()
    global num

    for i in range(1000000):

        # 上锁
        lock.acquire()
        # 同步的代码块最好要进行异常捕获保证最终能释放锁，否则有可能代码出错没有释放而导致死锁
        try:
            num += n
            num -= n
        finally:
            # 释放锁
            lock.release()

        # 使用with简化上述代码，功能相同
        # with lock:
        #     num += n
        #     num -= n

    print(threading.current_thread().name, "结束")


if __name__ == "__main__":

    print(threading.current_thread().name, "主线程运行")
    t1 = threading.Thread(target=run, name="子线程1", args=(5, ))
    t2 = threading.Thread(target=run, name="子线程2", args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(num)
    print("主线程结束")








