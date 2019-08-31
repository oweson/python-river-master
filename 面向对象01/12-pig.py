class Pig:
    def __init__(self, new_age, new_name):
        print('is---------------------------')
        self.age = new_age
        self.name = new_name

    def __str__(self):
        msg = "年纪是%d" % (self.age)
        return msg


ppx = Pig(21, 'ppx')
print(ppx)
