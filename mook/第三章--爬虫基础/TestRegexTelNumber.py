import re

num = "15797624891"
num2 = "12797624891"
regex_str = "(1[590][1-9]{9})"
# {9}出现9次任意
mynum = re.match(regex_str, num2)
if mynum:
    print(mynum.group(1))
# [^ 1]不为1，出现9次
ppx = "你 好"
regex_str03 = "你\s好"
# \s和\S都是匹配一个字符，第一个可以有空格，第二个是不为空格进行匹配
b = re.match(regex_str03, ppx)
# 只匹配一个空格
if b:
    print("hahahah")
k = "你sssssssssssssssss好"
regex_str04 = "你\S+好"
result = re.match(regex_str04, k)
if result:
    print(result)
