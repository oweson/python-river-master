import re

regex_str = "[pP]ython"
regex_str01 = "[0-9]{2}"
regex_str02 = "\D{6}"
regex_str03 = "\d{11}"
c = re.match(regex_str03, "12312312390")
print(c)
b = re.match(regex_str02, "hellop")
print(b)
line = "python"
result = re.match(regex_str, line)
a = re.match(regex_str01, "123123")
print(a)
if result:
    print(result)
print("-----------------------")
regex="\w{6}"
regex="\W{15}"
line="12334,asaksjaks____,,,,,"
line=",,,,,,,------,,,,,,,````````12334,asaksjaks____,,,,,"
print(re.match(regex,line))
