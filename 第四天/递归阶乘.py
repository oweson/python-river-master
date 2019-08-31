result=1
def ppx(num):
    global result
    result= 1
    if num != 1:
        result = num * ppx(int(num - 1))
    else:
        return result


a = ppx(1)
b = ppx(10)
print(a)
print(b)
