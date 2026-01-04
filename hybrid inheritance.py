
class dad():
    def money(self):
        print("Dads Money")

class land():
    def important():
        print("Son1 land")

class son1(dad,land):
    def laptop(self):
        print("Son1 Laptop")

# here son1 is multiple inheritance and hierarchecal inheritance
# so it is called hybrid inheritance



class son2(dad):
    def laptop(self):
        print("Son2 Laptop")



class son3(dad):
    def laptop(self):
        print("Son3 Laptop")

# if many class inherits one class its hierarcheal inheritance

s2=son2()
s2.laptop()
s2.money()
