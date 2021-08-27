
'''程序可以访问、监测。和修改它本身状态或行为的一种能力（自省）
    简言之就是：可以通过  字符串的形式  来操作（增删改查）一个对象的属性


    反射方法：
        1. getattr（）查
        2。 hasattr（）查
        3， setattr（）改
        4， delattr（）删

    作用：假如有一些指令由用户决定，（外部指令都有字符串组成）

'''
class Person():
    def __init__(self,name,age):
        self.name  = name
        self.age  = age



p = Person("Alex",22)
# 如何判断类中有没有name等未知的属性，因为在外部是看不到类的内部
# 实现,使用反射中的一个方法，hasattr（对象，“属性名”），还有getattr（）
if hasattr(p,"name1"):
    print("xxxxxxxx")


# ！！！！！！！！！！！！！！！！！！！！
# hasattr()
# 通过一个字符串就可以调用函数
'''
user_command = input(">>:").strip()
if hasattr(p,user_command):
    # 返回的是一个函数
    func = getattr(p,user_command)
    # 调用函数
    func()

'''


# ！！！！！！！！！！！！！！！！！！！！
# setattr()
# 可以在类的外部定义函数，然后绑定到某一个类中

def talk(self):
    print(self.name,"is talking")

setattr(p,"talk",talk)
# 如果是使用实例p，则调用函数时要传入self 也就是传p，否则类不会自动加self
p.talk(p)
# 如果传的是类名Person的话就不用在调用时加参数
setattr(Person,"speak",talk)
p.speak()




# ！！！！！！！！！！！！！！！！！！！！
# delattr()
# 以下两种一个意思
del p.age
delattr((p,"age"))












