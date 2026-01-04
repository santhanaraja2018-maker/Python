
a=[]
sum=0
print ("Enter 10 Numbers")
for i in range(10):
    num= int(input("Enter Number " +str(i+1)))
    """ here we have done casting as integer cannot add with string"""
    a.append (num)
    
print(a)

for i in a:
    sum=sum+i
print("Sum of Numbers : ",sum)

