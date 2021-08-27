
'''       反射  很重要 ！！！！！！  '''
'''
如何反射一个文件下指定字符串对应的属性
'''
# getattr("xxx.py","属性名")


'''补充知识点'''
print(__name__)
'''输出结果： __main__ 就代表模块本身 相当于self，但是和实例有区分，不可调用'''





# 有时候会莫名其妙在别人的代码里见到以下语句，实际上的作用是测试
# 测试这个文件是被别人执行还是自身主动执行
# 被别人导入就只会返回该模块名，见test.py，
# 自身主动执行就会输出  哈哈哈
# if __name__ == '__main__':#只会在被别的模块导入的时候这句判断才有意义
#     print("哈哈哈")




import sys

# for k,v in sys.modules.items():
#     print(k,v)

# print(sys.modules["__name__"])


import __test
if hasattr(__test,"sayhi"):
    f = getattr(__test,"sayhi")
    f()


