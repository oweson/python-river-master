s = "hello,world"
for i in s:
    print(i)
a = [1, 2, 3, 4, 5, 6]
for b in a:
    print("------------")
    if b == 4:
        break
    print(b)
x = [1, 2, 3, 4, 5, 9,10,11,12]
for opop in x:
    print('================')
    if opop == 5:
        print("5以后的不会执行了！！！")
        break
    print(opop)
