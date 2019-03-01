# 第一题
import os
path="test.text"
C=open("test","r+")
while True:
    str=C .readline()
    if str=="":
        break
    elif str[0]=="#":
        continue
    else:
        print(str, end="")
C.close()
# 第二题
import os
path="D:\\img"
# name=print(os.path.isdir(path))
# print(os.listdir(path))
while True:
    list1=os.listdir(path)
    print(os.listdir(path))
    for i in list1:
        print(i)
        os.rename(path+os.sep+i,path+os.sep+"py_"+i)
    break

