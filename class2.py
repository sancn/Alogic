class person:
        def __init__(self):
            self.name='ram'
            self.age=23
            self.height=5.7
    
        def details(self):
            print(f"Name: {self.name}, Age:{self.age}")

        def person_details(self,name,age):
            self.name=name
            self.age=age
            print(f"Name: {self.name}, Age:{self.age}")


p_obj=person()
p_obj.details()
p_obj.person_details('san',23)