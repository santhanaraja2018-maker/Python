class AdamNumber():
    def __init__(self,n):
        self.n = n

    def  reverse(self,num):
        rev =0
        while (num > 0):
            digit = num%10
            rev = digit + (rev*10)
            num  = num//10
        return rev
    
    
    def genaerate_Adams_Number(self):
        rev_n = self.reverse(self.n)
        print(rev_n)
        square = self.n*self.n
        print(square)
        rev_square = rev_n*rev_n
        print(rev_square)
        rev_result_rev_square = self.reverse(rev_square)
        print(rev_result_rev_square)

        

        if( square == rev_result_rev_square):
            print("The number ",self.n," you entered is Adams number ")
        else:
            print("The number ",self.n," you entered is not Adams number ")

        
n= int(input("Enter Number : "))
    
child = AdamNumber(n)
child.genaerate_Adams_Number()
    
    



