def printStar():
    print("$" * 10)


def mainFun():
    i = 0
    while i < 10:
        printStar()
        print("这是第%d次输出" % i)
        i += 1


mainFun()
