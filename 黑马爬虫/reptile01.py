import urllib.request
f = urllib.request.urlopen('http://www.baidu.com')
# 因是Python3里的urllib模块已经发生改变，此处的urllib都应该改成urllib.request。
firstLine = f.readline()
print(f.read())
print(firstLine)
print(f.info())
print(f.geturl())
print(f.getcode)
f=urllib.request.urlretrieve("https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E6%9E%97%E5%85%81%E5%84%BF&step_word=&hs=2&pn=18&spn=0&di=16006632290&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=3682156789%2C519227332&os=1930142634%2C3284764450&simid=0%2C0&adpicid=0&lpn=0&ln=3780&fr=&fmq=1538557101747_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=star&bdtype=0&oriquery=&objurl=http%3A%2F%2Fdingyue.nosdn.127.net%2Fx6p4sCO7FVPNdZlQSoqhCLozStMFhOLFvLiAdO2HqJs6u1527064419915.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3F1y_z%26e3B8mn_z%26e3Bv54AzdH3FedAzdH3Fw6ptvsjAzdH3F1jpwtsAzdH3FDIGMGKmUacd8HT0I_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=",filename="ppng")
print(f)
