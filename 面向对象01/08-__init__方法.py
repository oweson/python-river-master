class Cat:
    """定义了一个Cat类"""

    # 1 初始化对象,类似构造函数的java
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    # 2 方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%d" % (self.name, self.age))


# 3 创建一个对象
tom = Cat("汤姆", 40)
tom.eat()
tom.drink()
# tom.name = "汤姆"
# tom.age = 40
tom.introduce()

lanmao = Cat("蓝猫", 10)
# lanmao.name = "蓝猫"
# lanmao.age = 10
lanmao.introduce()

ppx = Cat("程万里", 24)
ppx.eat()
ppx.introduce()
print(ppx.name)
