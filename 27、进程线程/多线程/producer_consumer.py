import threading
import queue, time, random

'''
队列 多线程实现生产者消费者
'''

lock = threading.Lock()


def producer(id, q):

    num = 100
    while num > 0:
        q.put(num)
        time.sleep(3)
        print("生产者%d生产了数字%d" % (id, num))
        num -= 1

def consumer(id, q):

    while True:
        time.sleep(3)
        lock.acquire()
        if q.empty():
            print("暂无数字可消费，消费者%d正在等待" %id)
            lock.release()
            continue
        else:
            item = q.get()
            print("消费者%d消费了数字%d" % (id, item))
            lock.release()



if __name__ == "__main__":

    q = queue.Queue()

    for i in range(1, 2):

        threading.Thread(target=producer, args=(i, q)).start()

    for i in range(1, 4):

        threading.Timer(2, consumer, args=(i, q)).start()

