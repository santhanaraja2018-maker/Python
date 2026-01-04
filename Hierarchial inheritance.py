
class dad():
    def money(self):
        print("Dads Money")


class son1(dad):
    def laptop(self):
        print("Son1 Laptop")



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
