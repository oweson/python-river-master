a = 100


def add():
    a = 200
    print(a)
    a -= 1
    print(a)


add()
print(a)
'''修改的是局部变量，局部优先'''


def substrac():
    global a
    a -= 1
    a += 101
    print(a)
    '''强龙不压地头蛇就是局部变量'''


substrac()
print(a)
