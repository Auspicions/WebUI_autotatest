# 一、文件流的os 模块

import  os
#面试：模块 os

# 1.创建文件夹
# os.mkdir("d://doc2")
# 多层
# os.makedirs("d://doc2/a/b/c")


# 2.删除
# os.rmdir("d://doc2/a/b")
# os.removedirs("d://doc2/a/b/c")

# 扩展：递归  遍历出c盘所有文件

# 3.改名
# os.renames("d://doc","d://doc3")

# 文件改名
# os.renames("d://doc","d://doc3")

# os.remove("d://doc3/a.txt")

# 了解：
# 获得当前系统 #posix -> linux或者unix系统  nt -> window系统
# print(os.name)
# 获得文件的绝对目录
# print(os.getcwd())
# 获得目录中的文件名称
# print(os.listdir())
# print(os.listdir("d:\\")) #指定目录
path="d:"+os.sep+"doc5"
os.mkdir(path)

# print(os.sep)  win:\  linux:/



# 二、os子模块

import  os

path="d:\\doc2\\b.txt"
# print(os.path.isfile(path))   #文件
# print(os.path.islink(path))  #快捷方式
# print(os.path.isdir(path))  #文件夹
# print(os.path.isabs(path)) #是不是绝对路径  C:\\
print("--------")
# print(os.path.exists(path)) #文件是否存在
# print(os.path.getsize(path)) #文件大小
print(os.path.split(path))

# 扩展：
print(os.path.getctime(path)) #文件创建时间
print(os.path.getmtime(path)) #修改  1543714827.45928
print(os.path.getatime(path)) #访问  1543714827.45928

import  time
t=os.path.getctime(path)
# print(time.localtime())
t2=time.localtime(t)
# 格式化
print(time.strftime('%Y-%m-%d  %H:%M:%S',t2))
import os

# print(os.getcwd())
# print(os.listdir("D://")) #指定目录
# print(os.path.exists("doc")) #文件是否存在
path="D://day1202//doc"
A=(os.path.isdir(path))
if A==True:
    C=open("D://day1202//doc//io.doc","w+")
    C.close()
else:
    os.makedirs("D://day1202")
    C=open("D://day1202//doc//io.doc","w+")
    print("创建成功")
    C.close()