import threading

'''
    Timer指定线程启动延时，单位为秒
'''

def run():

    print("子线程运行")


if __name__ == "__main__":

    threading.Timer(5, run).start()
    