import threading, time

'''
Semaphore 控制线程信号量，表示同时只能有几个线程运行
'''
# 创建信号量 指定2个
sem = threading.Semaphore(2)

def run():

    # 同时就只能有两个线程运行
    with sem:
        for i in range(5):
            print("%s---%d" % (threading.current_thread().name, i))
            time.sleep(1)

if __name__ == "__main__":

    for i in range(5):
        print("创建并启动线程", i + 1)
        threading.Thread(target=run).start()