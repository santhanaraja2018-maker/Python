class calculator:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def add(self):
        print("Add : ", self.num1+self.num2)

    def sub(self) :
        print("Sub : ",self.num1-self.num2)


Operation=calculator(45,25)
Operation.add()
Operation.sub()
