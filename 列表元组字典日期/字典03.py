'''1 字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割， ,
分割，整个字典包括在花括号 {} 中 ,'''
dict = {1: 'a', 2: 'b'}
'''2 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。'''
print(dict[1])
'''3 添加'''
dict[3] = 'ppx'
'''4 修改'''
dict[1] = 'xiaoming'
print(dict)
'''5 delete:del dict['Name']  # 删除键是'Name'的条目
dict.clear()      # 清空词典所有条目
del dict          # 删除词典'''
'''6 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住;
和map相似会覆盖！'''
'''7 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行'''


