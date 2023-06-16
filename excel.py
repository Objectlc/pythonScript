import openpyxl
import os

path1=input("请输入你想归总的文件目录：")
path2=input("请输入你想归总在那个文件的路径：")

workbook2=openpyxl.load_workbook(path2,read_only=False)
workshell2=workbook2["Sheet1"]

for file in os.listdir(path1):
    fileName=file.split(".")
    if (not(os.path.isdir(path1+"/"+file)) and fileName[1] == "xlsx" and path1+"/"+file!=path2):
        print(file)
        workbook1 = openpyxl.load_workbook(path1+"/"+file)
        workshell1 = workbook1.active
    else:
        continue
    for r in workshell1:
        temp = []
        for l in r:
            temp.append(l.value)
        workshell2.append(temp)
workbook2.save(path2)
