class Cat:
    # 1 属性
    id = 21
    age = 24

    # 2 方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%d" % (tom.name, tom.age))


# 3 创建一个对象
tom = Cat()

# 4 调用tom指向的对象中的 方法
tom.eat()
tom.drink()

# 5 给tom指向的对象添加2个属性
tom.name = "汤姆"
tom.age = 40

# 6 获取属性的第1种方式
# print("%s的年龄是:%d"%(tom.name, tom.age))
print("%s的年龄是%d" % (tom.name, tom.age))

# 7 tom.introduce()
print("-------------------------")
print(tom.introduce())
