file = open("E:\BaiduNetdiskDownload\ppx.txt", 'r')
p = file.readline()
i = 1
for tem in p:
    print("%d,  %s" % (i, tem))
    i += 1
file.close()
