import threading, time

'''
Barrier 凑够n个线程才继续执行
'''
# 指定凑足3个线程后继续执行
bar = threading.Barrier(3)


def run():
    # 同时就只能有两个线程运行

    print("%s---" % threading.current_thread().name)
    time.sleep(1)

    bar.wait()

    print("%s结束" % threading.current_thread().name)


if __name__ == "__main__":

    for i in range(5):
        print("创建并启动线程", i + 1)
        threading.Thread(target=run).start()


'''
由于同时创建了5个线程，而凑数为3，因此最终会有三个线程执行结束，剩余2个线程由于凑不够3个一直等待
'''