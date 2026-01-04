
class a():
    def __init__(self):
        print("A")
    def display(self):
        print("You are in Class A")

# here even if we inherit class a in b it will load only constructor b
# if there is no constructor in b then it will load parent constructor
# if there is constructor in b it wont load parent
# if we need to acces parent constructor even if you have constructor in child use super keyword


class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("You are in Class B")

#here even if inherits a & b super key word loads only A constructor
#only the (a,b) first class contrutors will be called if we use super in multiple inheritance

class c(a,b):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("You are in Class C")
        
obj1=c()
