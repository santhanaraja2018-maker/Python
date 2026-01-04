class phone:

    chargertype= "C-Type"  #class variable
    def __init__(self,brand,price):
        self.brand=brand   #instance variable
        self.price=price   #instance variable
        

    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
        print("Chaergertype: ",self.chargertype)


phone.chargertype = "B-Type" # class varible can be modified by using class name

samsung = phone("Samsung",100000)
samsung.display()

redmi = phone("redmi", 60000)
redmi.display()

google = phone("pixel", 200000)
google.display()
        
