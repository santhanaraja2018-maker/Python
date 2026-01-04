class Animal():
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Bird(Animal):
    def sound(self):
        print("Birds sign")
        
# here it is method overriding
# same method written in both class if we call by animal first method executes
# if we call by animal second method executes

a1=Animal()
a1.sound()
d1=Dog()
d1.sound()
b1=Bird()
b1.sound()
