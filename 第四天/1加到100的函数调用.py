def add(num):
    sum = 0
    i = 1
    while i < num:
        sum += i
        i += 1
    return sum


result = add(101)
print("1---100的和是%d"%result)
