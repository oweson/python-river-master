class Cat:
    """定义了一个Cat类"""

    # 1 初始化对象
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        msg = "%s的年龄是：%d" % (self.name, self.age)
        return msg

    # 2 方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%d" % (self.name, self.age))


# 3 创建一个对象
tom = Cat("汤姆", 40)

lanmao = Cat("蓝猫", 10)

print(tom)
print(lanmao)
print(id(tom))
