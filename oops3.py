class vehicle():
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("Car started")

c1=car()
c1.start()
    
v1=vehicle()
v1.start()
