import urllib.request

url = "http://www.baidu.com/s"

request = urllib.request.Request(url)
result = urllib.request.urlopen(url)
print(result.read())
print((result))
