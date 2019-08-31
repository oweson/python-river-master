class Pig:
    def __init__(self, name, color='red'):
        self.name = name
        self.color = color

    def __del__(self):
        print("收垃圾啦")

    def run(self):
        print("%s在田野里奔跑！" % self.name)


class PigSon(Pig):
    # 继承了pig
    def setName(self, name):
        assert isinstance(name, object)
        this.name = name

    def eat(self):
        print('%s在吃饭' % self.name)


oweson = PigSon("ppx")
oweson.eat()
oweson.run()
# 私有地属性被继承了
print(oweson.color)
