# file = input('请输入')
# print(file)
str = "hello,world"
# 1 字符串查找
result = str.find("hello", 0, 10)
print(result)
# 2 替换
result = str.replace("hello", "hi", 2)
print (result)
mystr = "hello"
result = mystr.ljust(10)
print(result)
result = mystr.center(100)
print (result)
