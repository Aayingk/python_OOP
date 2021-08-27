'''
1.类名开头字母大写
2.类方法第一个参数必须是  self self代表实实例本身
'''


# 定义类模板
class Dog:
    d_type = '京巴'             #类属性：公共属性（例如：狗的名字就不能写成类属性）
    def __init__(self,name,age):
        print('haha',name,age)
        self.name_nixx = name       #这是一个绑定操作，利用self绑定后，name就在实例化的时候存储在了实例中

    def say_hi(self):          #self 代表实例本身
        print('hello,i am a dog ,my type is',self.d_type)



#生成一个实例
# d = Dog()
# # 实例.方法
# d.say_hi()

d2 = Dog('maodan',20)