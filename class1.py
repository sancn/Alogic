# class mob_detail:
#     def __init__(self):
#         self.model='redmi'
    
#     def show_detail(self):
#         print('Model is:',self.model)

# mob=mob_detail()
# mob.show_detail()


class person:
    def __init__(self):
        self.name="Ram"
        self.age=23
        self.height=5.7

    def details(self):
        print(f"Name: {self.name},age: {self.age}, Height: {self.height}")

p=person()
# print(getattr(p, 'details', None)())
# p.hero = "name"
# print(getattr(p, 'hero'))
p.details()
# print(p.hero)

        