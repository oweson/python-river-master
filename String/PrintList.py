list = [1, 'hello', "world"]
''' 1 列表的数据类型可以不相同！'''
print(list[0])
print(list[1])
print(list[2])
''' 2 for循环输出'''
for num in list:
    print(num)
''' 3 while输出'''
length = len(list)
i = 0
while i < length:
    print(list[i])
    i += 1
'''4 添加元素 append'''
nums = int(input("输入年龄......"))
list.append(nums)
for num in list:
    print("添加后的元素是")
    print(num)
''' 5 追加元素，一个或者整个的放入！'''
b = [1, 3, 5]
list.append(b)
'''6 一个一个的放入'''
list.extend(b)
for one in list:
    print(one)
''' 7 插入'''
list.insert(2, "ppx")
''' 8 修改'''
list[0] = 'pig is comming'
print(list)
