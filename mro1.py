#concept of single inheritance
class A():
    def method(self):
        print("method A() called")
class B(A):
    pass
    # def method(self):
    #     print("method B() called")
obj=B()
obj.method()
