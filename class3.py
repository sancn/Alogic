class person:
        def __init__(self,name,age,height):
            self.name=name
            self.age=age
            self.height=height
    
        def details(self):
            print(f"Name: {self.name}, Age:{self.age}, Height:{self.height}")


p_obj=person('ram',23,5.7)
p_obj.details()
