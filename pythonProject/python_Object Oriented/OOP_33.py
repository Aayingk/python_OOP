'''       双下划綫方法  （类的内置方法）       '''
''''''





class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __len__(self):
        print("trigger")
        return 2
    def __hash__(self):
        print("hash...")
        return 22222

    def __eq__(self, other):
        print("是否相等")

p = Person('ALEX',22)
p2 = Person("jsck",22)
print(len(p))
print(p.__eq__(p2))
'''C:\ProgramData\Anaconda3\envs\pythonProject\python.exe "D:/pythonProject/python_Object Oriented/OOP_33.py"
trigger
Traceback (most recent call last):
  File "D:/pythonProject/python_Object Oriented/OOP_33.py", line 17, in <module>
    print(len(p))
TypeError: 'NoneType' object cannot be interpreted as an integer'''
# 以上报错加return 2 就可以解决


