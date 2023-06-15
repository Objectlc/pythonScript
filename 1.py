import os

path=input("请输入你想拷贝的路径： ")
fpath=input("请输入你想存储的路径以及文件名： ")

def fileContentCopy(path):
    fn = os.listdir(path)
    for filename in fn:
        filePath=path + "/" + filename
        if os.path.isfile(filePath):
            with open(filePath, "r", encoding="utf-8") as content:
                f1 = content.read()
            with open(fpath, "a", encoding="utf-8") as content:
                content.write(f1 + "\n")
        if os.path.isdir(filePath):
            fileContentCopy(filePath)

fileContentCopy(path)