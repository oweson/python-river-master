list = [1, 2, 3]
if 2 in list:
    print("找到啦")
else:
    print("找到个鬼！")
''' 2 查找索引和统计，index和count'''
b = list.index(1, 0, 3)
# 索引在0的位置；
print(b)
# 统计出现的次数；
c = list.count(1)
print(c)
