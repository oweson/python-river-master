import math
from math import ceil
from Fish import ppx
from msgnew import *

# from math import *
test1()


def a():
    ppx()


print('=================')
ppx()
print('================')
a()
c = ceil(101.1212)
print(c)

a = math.sin(100)
print(a)
'''dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
返回的列表容纳了在一个模块里定义的所有模块，变量和函数'''
content = dir(math)
print(content)
'''包是一个分层次的文件目录结构，它定义了一个由模块及子包，
和子包下的子包等组成的 Python 的应用环境。
简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。
__init__.py 用于标识当前文件夹是一个包。'''
