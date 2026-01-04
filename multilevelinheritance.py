#multilevel inheritance

class grandpa():
    def phone(self):
        print("Grandpa's phone")

class dad(grandpa):
    def money(self):
        print("Dads money")

class son(dad):
    def laptop(self):
        print("Son's Laptop")

ram = son()
ram.laptop()
ram.money()
ram.phone()
