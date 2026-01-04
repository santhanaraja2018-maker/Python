class laptop():
    chargertype = "C-Type"

    def __init__(self):   #using self keyword are all insatnce methods
        self.brand = ""
        self.price = 34

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)

# class methods are rarely used and finded by cls keyword
    @classmethod  #decorators
    def changeChargerType(cls):
        cls.chargerType="B-Type"
        print("Charger type changed to B")

    @staticmethod  #decorators
    def info():
        print("This is static method")

hp=laptop()
hp.setPrice(20000)
hp.getPrice()


#for call class method we have to pass the class name
#laptop.changeChargerType(laptop)
#else we can use decorators @classmethod then we can call like instance method

laptop.changeChargerType()
hp.info()

# instance method is default and no decorators needed
# for clas  and static method we need to use decorators
