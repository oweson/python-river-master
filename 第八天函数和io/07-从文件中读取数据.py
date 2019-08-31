f = open("heihei.txt", "r")

content = f.read()
print(content)

f.close()
# 关闭文件流
f = open("happy.txt", 'r')
content = f.read()
print(content)
f.close()
