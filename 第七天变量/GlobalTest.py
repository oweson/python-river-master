age = 0


def changeAge():
    global age
    age = 24
    print("my age  is %d" % age)


def height():
    return 172


changeAge()
result = height()
print("我的身高是%d" % result)
