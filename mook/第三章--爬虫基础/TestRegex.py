import re

line = "bbboay123"
regex_str = "^b.*3$"
if re.match(regex_str, line):
    print('yes')
# 匹配3结尾的字符串
ppx = "abcdefg3"
regex_str02 = ".*3$"
if re.match(regex_str02, ppx):
    print("yes")
else:
    print("no")
# python贪婪匹配
# 从最左边开始匹配；

