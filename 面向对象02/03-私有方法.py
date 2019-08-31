class Dog:

    # 1 私有方法
    @staticmethod
    def __send_msg():
        print("------正在发送短信------")

    # 2 公有方法
    def send_msg(self, new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print("余额不足,请先充值 再发送短信")

    @staticmethod
    def eating(self):
        print("eating meat")


dog = Dog()
dog.send_msg(100)
dog.eating(self=200)
dog.send_msg(100)
