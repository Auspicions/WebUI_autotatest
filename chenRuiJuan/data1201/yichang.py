# try:
#     1/0
# except ZeroDivisionError as e:
#     print("异常处理----------")
# else:
#     print("正常执行------")
# finally:
#     print("不管你运行是否，我正常执行")
# print("继续执行。。。。")
# 自定义异常
class ShortException(Exception ):
    def __init__(self,msg):
        self.msg=msg
class Student:
    def setld(self,id):
        if len(id)==8:
            self.id=id
        else:
            raise ShortException("id的长度必须是8位")
try:
    stu=Student()
    stu.setld("20246542")
    print("id:",stu.id)
except ShortException as e:
    print(repr(e))