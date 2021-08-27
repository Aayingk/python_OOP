'''
依赖关系
class Dog:
    def __init__(self,name,age,master):
        self.name = name
        self.age = age
        self.master = master   #master 传进来的应该是个对象    此处是依赖关系的体现，，重点
        self.sayhi()          #调用自己的方法在实例化的时候
    def sayhi(self):
        print('Hi,im %s ,my master is %s '%(self.name,self.master))


class People:
    def __init__(self,name):
        self.name = name
'''



'''
关联关系
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.partaner = None    #此处应初始化一个对象，但是没有之前初始化为NONE

P1 = Person('KK',24)
P2 = Person('ll',23)

# 手动 双向绑定对象关系
P1.partaner = P2
P2.partaner = P1
'''



'''
组合关系
由一堆组件构成一个完整的实体，组件本身独立，但是不能自己运行必须跟宿主组合运行
class weapon:
    def dog_stick(self,dog):
#         打狗棒
        pass
    def  print_log(self,obj):
#         输出掉血多少等信息

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 组合的中重点在这里，weapon就相当于人的器官，是一个组件
        self.weapon = weapon()          #注意此处在实例化person时同步实例化。

p = Person('SSS',23)
print(p.weapon.dog_stick())             #输出打狗棍
'''


















