'''     动态创建一个类      '''
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age





'''type是所有类的祖师爷，包括object，所有类都是type产生的'''
p = Person("jack",23)
print(type(p))
# <class '__main__.Person'>
print(type(Person))
# <class 'type'>






def __init__(self, name, age):
    self.name = name
    self.age = age

'''所以可以通过type动态产生一个类'''
dog_class = type("Dog",(object,),{"role":"dog","__init__":__init__})
print(dog_class)
# <class '__main__.Dog'>

d = dog_class("mjj",22)
print(d.role,d.name,d.age)







