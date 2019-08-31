import random

# # 1 随机数的测试
# i = 0
# while i < 10:
#     a = random.randint(0, 2)
#     print(a)
#     i += 1
# # 0,1,2三种之间的生成！


# 2 小测试
# 三个办公室
list = [[], [], []]
# 八位老师
names = [1, 2, 3, 4, 5, 6, 7, 8]
for name in names:
    result = random.randint(0, 2)
    list[result].append(names)
i = 1
for a in list:
    print("办公室%d的人数是%d" % (i, len(a)))
    i += 1
    print(a)
