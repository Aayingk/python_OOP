
'''静态方法'''
'''
@staticmethod修饰的函数不能访问类变量也不能访问和实例变量
静态方法隔断了他和类或实例的任何关系，因为他连实例self都不传了，所以他其实有绑定才可调用的属性
'''

class Student(object):
    def __init__(self,name):
        self.name = name
    @staticmethod
    def fly(self):
        print(self.name,"is fiying")


s = Student("jack")
# 静态方法需要手动传self，也就是自身实例，否则在类实例化时候，
s.fly(s)
# 但是如果执行以下语句则会报错
# s.fly()












