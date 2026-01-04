class dad():
    def phone(self):
        print("Dad's phone")

class mom():
    def sweet(self):
        print("Mom's Sweet")
#if a class inherits another class its single inheritance
#if a class inherits another 2 or more class its multiple inheritance
        
class son(dad,mom):
    def laptop(self):
        print("son's phone")

ram=son()
ram.laptop()
ram.phone()
ram.sweet()
