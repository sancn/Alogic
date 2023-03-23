class A():
    def method(self):
        print("Method A() is called")
class B():
    pass
    # def method(self):
    #     print("Method B() is called")

class c(A,B):
    pass
    # def method(self):
    #     print("Method C() is called")
obj=c()
obj.method()

    
