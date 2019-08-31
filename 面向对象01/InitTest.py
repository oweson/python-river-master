class Fish:
    def eat(self):
        print("eat fish")

    def sleep(self):
        print("sleep")

    def __init__(self, name, age):
        self.name = name
        self.age = age


tom = Fish("ppx", 21)
tom.eat()
print(tom.name)
