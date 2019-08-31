import random

a = random.randint(0, 2)
'''前后闭'''
println(a)
b = int(input("0石头，1剪刀，2布"))
if ((a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1)):
    print("you great")
elif (a == b):
    print("same")
else:
    print("come again")
