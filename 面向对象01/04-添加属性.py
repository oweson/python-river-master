class Cat:
    # 属性

    # 方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")


# 1 创建一个对象
tom = Cat()

# 2 调用tom指向的对象中的 方法
tom.eat()
tom.drink()

tom.name = "汤姆"
tom.age = 40
tom.height = 172
ppx = Cat()
ppx.eat()
# 3 动态添加的属性属于某一个对象的；
tom.height
print(tom.age)

