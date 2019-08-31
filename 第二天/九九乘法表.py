import random as ppx

cat = ppx.randrange(1, 100)
print(cat)
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d" % (i, j, i * j), end='')
        j += 1
    print("\n")
    i += 1
    '''外行的控制行，是二维的，必须有递增'''
