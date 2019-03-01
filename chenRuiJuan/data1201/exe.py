# 第一种
# f=open("test")
# str=f.readlines()
# print(str)
# f.close()
# # 第二种
f=open("test")
str=f.read(2)
print(str)
f.close()
# # 第三种
# f=open("test")
# while True:
#     str=f.read(2)
#     print(str,end="")
#     if str=="":
#         break
# # 第四种
# f=open("test")
# str=f.readlines()
# print(str)
# 优化
# c=open("F:\\python\\1201\\test.txt.txt")
# while True:
#     str=c.readlines()
#     print(str,end="")
#     if str=="":
#         break
# frush 刷新
try:
    f=open("F:\\k3.jpg","rb")
    f2=open("F:\\day\\k3.jpg","wb")
    while True:
        b=f.read(5)
        f2.write(b)
        if b==b'':
            break
except Exception as e:
    print(e)
# finally:
#     f.close()
#     f2.close()
