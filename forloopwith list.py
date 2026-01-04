
number = int(input("Enter how many numbers you need to add : "))
a=[]
for i in range (1,number+1):
    a.append(i)
print(a)


sum=0

for i in a:
    sum=sum+i
print ("Sum of ",number," numbers are : ",sum)
