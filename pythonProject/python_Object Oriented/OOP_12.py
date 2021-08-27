class Animal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('''''''')

# 括号里的意思是继承了Animal类
class Person(Animal):
    def own_func(self):
        print('子类独有方法')
    def eat(self):
        print('ssssssss')


# 以下语录会报错，因为你需要在实例化时传入Animal的三个参数
p = Person()

# 正确的实例化

p_right = Person('name',3,"M")
# 直接调用父类的方法
p_right.eat()



class Father:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def eat(self):
        print('爸爸吃')

# 括号里的意思是继承了Animal类
class Kid(Father):
    def __init__(self,name,age,sex,hobby):
        # 以下3 个语句是一个意思，都是继承
        Father.__init__(self,name,age,sex)
        # 以上的写法已经废弃了，改为以下形式
        super(Kid,self).__init__(name,age,sex)
        # 或者
        super().__init__(name,age,sex)
        self.hobby = hobby
    def eat(self):
        super().eat()     #执行父类的eat方法
        print('儿子吃')











