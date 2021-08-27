
'''__new__()方法
在——init——之前就执行'''
'''new 方法有什么作用：
        # __new__负责执行__init__
        # 在new中执行以下类实例初始化之前的操作
        #        
'''


# 实现单例模式
class Printer(object):
    tasks = []
    instance = None  #存放第一个实例
    def __init__(self,name):
        self.name = name
    def add_task(self,job):
        self.tasks.append(job)
        print("[%s] 添加任务[%s]到打印机，总任务数[%s]" %(self.name,job,len(self.tasks)))

    # 重写new后，输出p1p2p3的地址就相同了
    def __new__(cls, *args, **kwargs):
        #只有第一次实例化的时候，正常运行，后面每次实例化，并不真正创建一个新实例
        if cls.instance is None:
            # 进行正常的实例化，并把实例化后的对象，存放在cls.instance里
            obj= object.__new__(cls)
            print("obj",obj)
            cls.instance = obj   #把实例化后的对象存下来
        return cls.instance  #以后的每次实例化，直接返回第一次存的实例对象


p1 = Printer("word")
p2 = Printer("pdf")
p3 = Printer("excel")

p1.add_task("word file")
p1.add_task("pdf file")
p1.add_task("excel file")
print(p1,p2,p3)
# <__main__.Printer object at 0x000002095C7AA6D0> <__main__.Printer object at 0x000002095C7AA5E0> <__main__.Printer object at 0x000002095CA6A610>
# 3个实例地址，地址不同，但是干的是一件事 很浪费资源，
# 通过new实现单例模式后的输出
# <__main__.Printer object at 0x0000020140C9A130> <__main__.Printer object at 0x0000020140C9A130> <__main__.Printer object at 0x0000020140C9A130>




#
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#         print("正在执行init")
#
#     def __new__(cls,*args,**kwargs):
#         print("正在执行new")
#         print(cls,args,kwargs)
# #         <class '__main__.Student'>   类本身
# #         ('alex',)
# #         {}
# #        调用父类的new方法
#         return object.__new__(cls)
#
# p = Student("alex")
# # 可以看到只执行了new函数，并没有执行init函数
# # 原因，因为我们重写了new，而在重写之前init由原始的new方法自动调用
















