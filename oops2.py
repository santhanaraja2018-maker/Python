class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class manager(employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.dept)
        
m1=manager("Raja",80000,"EEE")
m1.display()
