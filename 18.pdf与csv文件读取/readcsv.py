import csv

path = "/Users/cuixiaodong/PycharmProjects/PythonStudy/18.pdf与csv文件读取/employees.csv"


def readCSV(path):
    with open(path,"r") as f:
        content = csv.reader(f)
        for line in content:
            print(line)

readCSV(path)

def writeCSV(path, contentList):

    with open(path,"a") as f:
        wr = csv.writer(f)

        for rowData in contentList:
            wr.writerow(rowData)

newfile = "/Users/cuixiaodong/PycharmProjects/PythonStudy/18.pdf与csv文件读取/new.csv"
newData = [["崔",2,3],[4,5,6],[7,8,9]]

writeCSV(newfile,newData)


