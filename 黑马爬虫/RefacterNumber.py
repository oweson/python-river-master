import re

regex_str = ".*?(\d+)年"
# 匹配4个数字
regex_str02 = ".*?(\d{4})年"
# ？取消贪婪匹配，就是左边网右边查找
line = "2018年十月五号"
result = re.match(regex_str, line)
result02 = re.match(regex_str, line)
print(result.group(1))
print(result.group(1))
if result:
    print(result.group(1))
