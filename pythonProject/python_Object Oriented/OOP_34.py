
'''     需要重点会的双下划綫方法       '''


# ''        'str & repr        '''
# class School:
#     def __init__(self,name,addr,type):
#         self.name = name
#         self.addr = addr
#         self.type = type
#     def __repr__(self):
#         return 'School(%s,%s)' %(self.name,self.addr)
#
#     def __str__(self):
#         return '(%s,%s)' %(self.name,self.addr)
#
# s1 = School("学校1","北京","私立")
# print("from repr:",repr(s1))
# print("from str:",str(s1))
# print(s1)
# # str和repr的区别：
# # 当print函数调用时，obj.__str__()
# # repr或者交互式解释器调用时，obj.__repr__()
# # 如果__str__没有被定义，那么会使用repr来代替输出
# # 注意：这类方法的返回值必须是字符串，否则抛出异常



'''
当repr和str都被注释掉的时候的终端输出
C:\ProgramData\Anaconda3\envs\pythonProject\python.exe "D:/pythonProject/python_Object Oriented/OOP_34.py"
from repr: <__main__.School object at 0x00000281BB1EA6D0>
from str: <__main__.School object at 0x00000281BB1EA6D0>
<__main__.School object at 0x00000281BB1EA6D0>
Process finished with exit code 0'''

'''
不注释掉时的终端返回
C:\ProgramData\Anaconda3\envs\pythonProject\python.exe "D:/pythonProject/python_Object Oriented/OOP_34.py"
from repr: School(学校1,北京)
from str: (学校1,北京)
(学校1,北京)

Process finished with exit code 0'''




'''    析构方法   对象消逝的时候做处理'''
class School:
    def __init__(self,name,addr,type):
        self.name = name
        self.addr = addr
        self.type = type

    def __del__(self):
        print("对象被释放掉了")

s1 = School("学校1", "北京", "私立")
print("sssssssssss")
print("sssssssssss")
print("sssssssssss")
print("sssssssssss")
print("sssssssssss")
print("sssssssssss")
'''C:\ProgramData\Anaconda3\envs\pythonProject\python.exe "D:/pythonProject/python_Object Oriented/OOP_34.py"
sssssssssss
sssssssssss
sssssssssss
sssssssssss
sssssssssss
sssssssssss
对象被释放掉了

Process finished with exit code 0'''

# 可以发现，__del__自动执行当对象结束时 ，但是是在最后执行












