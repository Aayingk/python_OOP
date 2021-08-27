'''
多继承
'''
class Shenxian:
    '''神仙类'''
    def fly(self):
        print('神仙都会飞')

    def fight(self):
        print('神仙在打架')


class Monkey:
    '''猴子类'''
    def eat_peach(self):
        print('猴子都喜欢吃桃子')
    def fight(self):
        print('猴子在打架')



class MonkeyKing(Shenxian,Monkey):
    '''美猴王类'''
    def jindouyun(self):
        print('孙悟空在翻筋斗云')


swk = MonkeyKing()
swk.fly()
swk.eat_peach()
swk.jindouyun()
swk.fight()
'''输出结果：神仙在打架，因为在类的继承从左到右按顺序继承'''
