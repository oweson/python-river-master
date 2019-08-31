import Pig

class PigSon(Pig):
    # 继承了pig
    def setName(self, name):
        assert isinstance(name, object)
        this.name = name

    def eat(self):
        print('%s在吃饭' % self.name)


oweson = PigSon("ppx")
oweson.eat()
