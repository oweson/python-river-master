f = open("E:\BaiduNetdiskDownload\ppx.txt", 'a+')
f.write("我曾经想改变全世界")
f.close()
r = open("ppx.txt", "rb")
file = r.read(21)
print(file)


