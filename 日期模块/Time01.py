import time

a = time.time()
print('当前的时间戳为：', a)
'''2 获得本地的时间'''
localtime = time.localtime(a)
print('本地的时间：', localtime)
'''3 获得格式化的时间'''
localFormatTime = time.asctime(time.localtime(time.time()))
print('格式化的本地时间：', localFormatTime)
