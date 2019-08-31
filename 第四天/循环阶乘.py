def multi(num):
    i = 1
    result = 1
    while (i <= num):
        result *= i
        i += 1
    return result


sum = multi(9)
print(sum)
