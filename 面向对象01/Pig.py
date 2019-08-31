class Pig:
    def look(self):
        print("look beautiful")

    def haha(self):
        print("like hahahahha")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 记住啦是return！
    def __str__(self):
        return "%s的年纪是%d岁啦" % (self.name, self.age)


tom = Pig("ppx", 24)
tom.haha()
print(tom.age)
rabbit = Pig("xiaohua", 23)
print(rabbit)
