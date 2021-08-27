'''封装'''
class Person:
    def  __init__(self,name,age):
        self.name = name
        self.age = age
        self.__life_val = 100    #私有变量
    def get_life_val(self):
        print('生命值为：',self.__life_val)   #调用私有变量
        self.__breath()                    #调用私有属性

    def __breath(self):                     #把函数私有化
        print('我在呼吸')

a = Person('Alex',22)
# print(a.__life_val)   #执行时会报错，因为外部没办法直接调用私有属性，只有在类的内部才有使用的权限


# 非要在外部调用私有方法也可以
# 语法：实例名._类名_方法名（）
a._Person__breath()
# 也可以调用私有变量
a._Person__life_val = 10
# 实例创建后再创建私有属性并不成功，变量不具有私有性