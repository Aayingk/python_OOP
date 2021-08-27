
'''属性方法property（属性）'''
'''作用：把一个方法变成一个静态属性（变量）
    和普通变量的区别：普通变量顶一万基本就拉到了
                   但是有很多变量需要有变动，用函数转变量更方便操作
                   
    eg； 查机票的数据处理流
        1. 连接各机场航班信息
        2. 查询信息
        3. 对返回的信息的处理解析显示给用户
        
    用户关心的是 飞机的状态、价格
    flight.state = 到达
    # 每当用户想要查询以上信息的时候，数据都要经过相同的一些步骤返回给用户，这时候就可以用property去写一个数据处理的方法
        
        
    注意property变量不可以赋值

'''

class Student(object):
    def __init__(self,name):
        self.name = name
    @property
    def fly(self):
        state = 0
        print(self.name,"is fiying")


    @fly.setter#实现外部修改的
    def fly(self,status):
        self.status = status
        print(self.status)
        print(self.name, "is fiying")




s = Student("jack")
# 以下代码会报错
'''Traceback (most recent call last):
     File "D:/pythonProject/python_Object Oriented/OOP_28.py", line 18, in <module>
     s.fly()
     TypeError: 'NoneType' object is not callable'''
# s.fly()
# 正确调用
s.fly








