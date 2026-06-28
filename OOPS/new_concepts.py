class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

# outside the class --> Function
def greet(person):
    print("Hi my name is ",person.name ," and i am ",person.gender)
    p1=Person("Teena", "Female")
    return p1
 

