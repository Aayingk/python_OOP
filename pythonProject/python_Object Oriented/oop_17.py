class Dog(object):
    def sound(self):
        print('汪汪汪')

class Cat(object):
    def sound(self):
        print('喵喵喵')

# 用函数写多态不常见，多为用多态类实现多态
def make_sound(animal_obj):
    '''统一调用接口'''
    animal_obj.sound()


d = Dog()
c = Cat()
make_sound(d)
make_sound(c)


class Document(object):
    def __init__(self,name):
        self.name = name
    def show(self):
        raise NotImplementedError('sub class must implement abstract method ')



class Word(object):
    def __init__(self,name):
        self.name = name
    def show(self):
        raise NotImplementedError('sub class must implement abstract method ')


class Pdf(Document):
    def show(self):
        return 'show pdf contents'


pdf = Pdf('哈哈.pdf')
word = Word('嘿嘿.pdf')
