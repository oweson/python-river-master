class Base(object):
    def test(self):
        print("----Base")


class A(Base):
    def test1(self):
        print("-----test1")


class B(Base):
    def test2(self):
        print("-----test2")


class C(A, B):
    pass


c = C()
c.test1()
c.test2()
c.test()


class J20(A, B):
    # 多继承防止和父类继承的类重复
    pass


ppx = J20()

ppx.test1()
# 继承的传递性!
