class palindrome:

    def __init__(self):
        self.rev=0
    def is_palindrome(self,n):
        num=n

        while num>0:
            digit=num%10
            self.rev=(self.rev*10)+digit
            num=num//10

        return n == self.rev


n=int(input("Enter Number : "))
check=palindrome()

if check.is_palindrome(n):
    print (n," is Palindrome")

else:
    print (n," is not Palindrome")
        
        
        
    
