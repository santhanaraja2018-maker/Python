class teacher:
    def __init__(self,Name,Regno):
        self.name = Name
        self.regno = Regno

    def display(self):
        print("Name : ",self.name)
        print("Regno : ",self.regno)


t1=teacher("Raja","123")
t1.display()

t2=teacher("Nive",456)
t2.display()
