num = input("请输入你要打印的数字")
number = int(num)


def printStar(number):
    i = 1
    print("这是第%d" % i)
    print("-------------\n" * number)
    i += 1


printStar(number)
