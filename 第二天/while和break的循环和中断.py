sum = 0
'''只是打印递增，可以省略sum'''
i = 0
while i < 10:
    print("--------")
    i += 1
    if i == 4:
        break
    print(i)
# --------------- demo2
i2 = 0
sum2 = 0
while i2 < 100:
    print("**************")
    sum2 += i2 # index=0,0,1,1,2,3,3 5,
    i2 += 1
    if i2 == 4:
        break
    print(sum2)
