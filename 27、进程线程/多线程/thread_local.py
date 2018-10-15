import threading


'''
    threading.local()线程本地空间，每个线程内部独立使用
    通过本地空间定义的变量只在线程内部使用
'''

num = 0

# 定义线程本地空间
local = threading.local()


def run(n):

    # 将全局变量的值赋予本地变量
    local.x = num

    for i in range(1000000):
        local.x += n
        local.x -= n
    print(threading.current_thread().name, "local.x=", local.x)

if __name__ == "__main__":

    t1 = threading.Thread(target=run, name="线程1", args=(5, ))
    t2 = threading.Thread(target=run, name="线程2", args=(10, ))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(num)

'''
    通过线程本地变量，避免线程间的代码混乱，无需加锁同步
'''