from collections import OrderedDict
from pyexcel_xls import get_data
from pyexcel_xls import save_data

'''
一种读取和保存xls或xlsx的第三方包
pip install pyexcel-xls
会依赖安装xlrd, xlwt
'''

# 读取
def readxls(path):

    # 直接调用获取方法，返回一个OrderedDict 有序字典对象
    # 每个key即是xls中sheet页的名称，对应的value就是sheet页的内容
    xdata = get_data(path)
    print(type(xdata))

    # 使用字典的特性进行遍历
    for k in xdata.keys():


        sheet = xdata.get(k)
        # 每个xls页的内容是一个二维列表，每个元素表示一行，每行是一个列表
        print(type(sheet))

        print(k,":",sheet)







if __name__ == "__main__":

    path = "/Users/cuixiaodong/PycharmProjects/PythonStudy/19.excel文件读写/数据库信息汇总.xlsx"
    readxls(path)

    # 写入xls，这里的写入只支持xls，如果要支持xlsx的写入，需要安装pyexcel-xlsx pyexcel-xlsxw
    path1 = "/Users/cuixiaodong/PycharmProjects/PythonStudy/19.excel文件读写/1.xlsx"
    sheet = []
    row1 = ["name","age","sal"]
    row2 = ["cuixd","33","1800"]
    row3 = ["llj","34","2000"]

    sheet.append(row1)
    sheet.append(row2)
    sheet.append(row3)

    content = OrderedDict()

    content.update({"emp":sheet})

    save_data(path1, content)


