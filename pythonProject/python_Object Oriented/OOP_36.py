'''            CALL 方法            '''
class School:
    def __init__(self,name,addr,type):
        self.name = name
        self.addr = addr
        self.type = type

    def __call__(self, *args, **kwargs):
        print(self,args,kwargs)



s = School("学校1","北京","私立")
s()  #实例名（）就执行
# or
# School("学校1","北京","私立")()








