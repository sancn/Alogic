
class person:
        def __init__(self,name,age,height):
            self.name=name
            self.age=age
            self.height=height
    
        def details(self):
            print(f"Name: {self.name}, Age:{self.age}, Height:{self.height}")


p_obj=person('ram',23,5.7)
# print(p_obj)
print(getattr(p_obj,'name','shyam'))  #get the value of an object attribute
print(getattr(p_obj,'color','blue'))  #get the value of an object attribute



setattr(p_obj,'age',25)
print(p_obj.age) 

print(hasattr(p_obj,'age'))
# p_obj.details()
