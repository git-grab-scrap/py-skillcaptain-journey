class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        
    def disp_person(self):
        print(f"Person Class initialized with values \n Person.name: {self.name} \n Person.age: {self.age}")
        
Person("Ram", 123)
p1 = Person("Alice", 25)
p1.disp_person()
p2 = Person("Bob", 30)
p2.disp_person()
