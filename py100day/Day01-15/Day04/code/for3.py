"""

输入非负整数n计算n!

Version: 0.1
Author: 骆昊
Date: 2018-03-01

"""

n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))
total = 1
x = int(input('x='))
total = 1
for k in range(1, x):
    total *= k
print('%d!=%d' % (x, total))
