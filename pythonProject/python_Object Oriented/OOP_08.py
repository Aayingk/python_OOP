
class People:
    nation = 'TW'
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = People('MJJ',23)
p2 = People('zjj',25)
p1.nation = 'cn'
# 注意，p1去修改nation这个类属性,实际上是是为p1这个实例创建了一个新的实例属性，不会修改类属性
print(p1.nation)   #cn
print(p2.nation)   #TW