s = "hello,ppx"
'''continue遇到就不在继续往下走，而是镜像下一次的循环'''
for a in s:
    if a == 'p':
        continue
    print(a)

for oweson in s:
    if oweson == 'l':
        continue
    print(oweson)
