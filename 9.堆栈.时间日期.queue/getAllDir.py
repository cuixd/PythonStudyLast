import os.path
import collections

'''
使用栈结构进行目录的深度遍历
使用队列结构进行目录的广度遍历

深度遍历核心思想：
    栈结构后进先出，先进后出，在逐层遍历目录时，由于始终先处理最后进栈的数据，所以遍历会顺着一个目录分支不断深入，
    直到分支结束，回头进行前一分支的遍历，而最早进栈的分支将最后遍历，谓之深度遍历
广度遍历核心思想：
    队列结构先进先出，后进后出，在逐层遍历目录时，由于始终处理最早进队的数据，同一层级的目录依次进队，再依次出队，
    所以遍历会将每一层级的目录按照进队顺序逐个遍历，进而带着整个目录树同步深入，谓之广度遍历
'''


# 深度遍历
def getalldirbystackdeep(dir):

    # 使用列表pop()模拟栈
    stack = []
    stack.append(dir)

    while len(stack) != 0:

        # 取出最后一个进栈的数据
        curdir = stack.pop()
        # print("目录111:"+curdir)
        filelist = os.listdir(curdir)
        for filename in filelist:
            abspath = os.path.join(curdir, filename)
            if os.path.isdir(abspath):
                print("目录:"+abspath)
                stack.append(abspath)
            else:
                print("文件:" + abspath)


# 广度遍历
def getalldirbyqueuescope(dir):

    # 使用collections模块产生一个队列
    queue = collections.deque()
    queue.append(dir)

    while len(queue) != 0:
        # 取出最先进栈的数据
        curdir = queue.popleft()

        filelist = os.listdir(curdir)
        for filename in filelist:
            abspath = os.path.join(curdir, filename)
            if os.path.isdir(abspath):
                print("目录:"+abspath)
                queue.append(abspath)
            else:
                print("文件:"+abspath)

'''
两个方法的代码及其类似，唯一的区别在于循环取出时，一个是取出最右边的，也就是最后的数据；另一个是取出最左边的，也就是最早的数据
'''

getalldirbystackdeep("/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化/1")

print("#######################")
getalldirbyqueuescope("/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化/1")

