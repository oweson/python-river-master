import urllib.request
f = urllib.request.urlopen('http://www.baidu.com')
print(f.read())