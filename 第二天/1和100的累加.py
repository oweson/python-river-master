i = 0
sum = 0
while i < 101:
    sum += i
    i += 1
print("1加到100是%d" % sum)
a = 0
b = 0
# --------end--------
while a <= 100:
    if a % 2 == 0:
        b += a
    '''a+=1属于while的，注意缩进'''
    a += 1
print("1-100的偶数是：%d" % b)

# -----------------------sum 1-100
number01, sum02 = 0, 0
while number01 <= 100:
    sum02 += number01
    number01 += 1
print('sum02 is %d' % sum02)
# ======================
x01, x02 = 0, 0
while x01 <= 100:
    if x01 % 2 == 0:
        x02 += x01
    x01 += 1
print('1-100的偶数的和是%d' % x02)
