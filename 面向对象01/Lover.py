class Lover:
    age = 23
    height = 165
    weight = 98

    def __str__(self):
        msg = "我的恋人体重是%d" % (self.weight)
        return msg

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


oweson = Lover("裴秀智", 24, 165, 98)

print(oweson.name)
print(id(oweson))
print(oweson)
