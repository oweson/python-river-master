def unSureLength(a, b, *args):
    sum = a + b
    for nums in args:
        sum += nums
    print("总数是%d" % sum)


unSureLength(1, 2)
unSureLength(1, 2, 3)
unSureLength(1, 2, 4, 5, 6, 7, 8)
