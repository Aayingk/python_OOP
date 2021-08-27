'''isinstance 和 issubclass'''
# 1.isinstance
class Foo(object):
    pass

obj = Foo()
# 判断obj是不是Foo类型
print(isinstance(obj,Foo))


# 2. issubclass
class Bar(Foo):
    pass
# 判断Bar是不是Foo的子集
print(issubclass(Bar,Foo))



'''  异常处理   '''
# try:
#     # your code
# except Exception:
#     # 出错后要执行的代码

while True:
    try:
        num1 = int(input("n1>:"))
        num2 = int(input("n2>:"))
        res = num1+num2
        print("result",res)
    except Exception as err:
        print("输出值不合法，必须是数字")



'''  万能异常捕获  '''
# d = [1,2,3]

try:
    # 下语句会报错，但是运行前并不确定会报错
    a = d[4]
#     万能异常捕获
except Exception as e:
    print("发生错误")
# 没有发生任何一场则执行这里
else:
    pass
#不管有没有异常都会执行finally
finally:
    pass



'''     raise 主动触发异常'''

try:
    raise IndexError
except IndexError as e:
    print("捕获到异常")




'''捕获自定义的异常'''

class YoutubeError(BaseException):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

