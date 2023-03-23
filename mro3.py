class A():
    def method(self):
        print("Method A() is called")


class B():
    # pass
    def method(self):
        print("Method B() is called")


class C(A, B):
    pass
    # def method(self):
    #     print("Method C() is called")


class D(C, B):
    pass

    # def method(self):
    #     print("Method D() is called")
obj = D()
obj.method()




