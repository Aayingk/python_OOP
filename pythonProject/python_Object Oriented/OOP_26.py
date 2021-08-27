

'''后续内容均是面向对象部分最后的细节补充，内容如下：
    1。 类方法、
        静态方法、
    2.  属性方法property
    3.  神奇的反射
    4.  类的双下划綫方法
    5.  用type动态创建一个类
    6.  isinstance\issubclass
    7.  异常处理
'''

'''类方法
    1. 类方法是通过@classmethod装饰器实现，类方法和普通方法的区别是，类方法只能访问类变量，不能访问实例变量
    而普通方法是先看实例变量，后查看类变量
    2. 原因，在 @classmethod装饰的类方法中的 self，是代指类本身，而不是实例本身，
    而普通函数self是代指实例本身
    3. 有什么用？
    eg：每生成一个学生，stunum加一，所以上stunum应该是一个类变量
'''
class Dog(object):
    # 类变量
    name = "stupid_dog"
    def __init__(self,name):
        # 实例变量
        self.name = name
    # 标记eat函数为类函数
    @classmethod
    def eat(self):
        # self.name 是实例变量，所以以下语句会报错
        print("dog %s is eating ..."% self.name)
        ''' Traceback (most recent call last):
            File "D:/pythonProject/python_Object Oriented/OOP_26.py", line 30, in <module>
            d.eat()
            File "D:/pythonProject/python_Object Oriented/OOP_26.py", line 24, in eat
            print("dog %s is eating ..."% self.name)
            AttributeError: type object 'Dog' has no attribute 'name
            '''
        # 当在Dog类中加入类变量后，即name = "stupid_dog"，以上语句则可以运行，变量溯源为类变量



d = Dog("MJJ")
d.eat()


class Student(object):
    __stu_num = 0
    def __init__(self,name):
        self.name = name
        # 注意是Student.而不是self，如果是self则结果已知为1
        # Student.stu_num += 1
        # print("生成了一个新学生，", name, self.stu_num)

        # 在定义了类方法后且将stu_num变成私有变量（外部无法访问）如何实现stu加一
        self.add_stu()

    @classmethod
    def add_stu(cls):
        cls.__stu_num +=1
        print("stu_num为",cls.__stu_num)



s = Student("MJJ")
s1 = Student("MJJ1")
s2 = Student("MJJ2")

# 作弊，实际只有3 个学生，但是执行以下语句
# Student.stu_num += 1
# print(Student.stu_num)
# 所以为了防止作弊，将stu_num私有化，在类方法中加一（但是也没有防止作弊）可以看以下代码
Student.add_stu()
#解决方案
'''
 @classmethod
    def add_stu(cls,obj):
        if obj.name:
            cls.__stu_num +=1
            print("stu_num为",cls.__stu_num)
'''
#这时候Student是没有name的，所以不能调用add_stu方法







