class fibonaci_series:
    def __init__(self):
        self.n1=0
        self.n2=1
        self.list = [ self.n1,self.n2 ]

    def do_fibo_series(self,n):
        for i in range (2,n):
            self.list.append(self.list[i-1]+self.list[i-2])
        print(self.list[:n])


fibo=fibonaci_series()
fibo.do_fibo_series(7)
            
