'''成员变量'''
a = 12000


def test1():
    '''函数里面定义的是局部变量'''
    a = 100


def test2():
    print("a=%d" % a)


test1()
test2()

print("a=%d" % a)
