

class laptop:
    def __init__(self):
        self.price=0
        self.ram=""
        self.processor=""
        
    def display(self):
        print("Price : ",self.price)
        print("Ram : ",self.ram)
        print("Processor : ",self.processor)
        

""" here def init is a constructor it runs automatically once the object is created """
""" No need to call seperately once objected created it runs """
""" The main purpose of constructor is to initialize or assign values to data
members of that class """

        

hp=laptop()
dell = laptop()

hp.price=50000
hp.ram = "6GB"
hp.processor = "i5"
hp.display()


dell.price=70000
dell.ram = "8GB"
dell.processor = "i7"
dell.display()
