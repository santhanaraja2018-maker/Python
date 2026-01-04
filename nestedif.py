salary = int(input("Enter your salary : "))
age = int(input("Enter your age : "))

if (salary >=20000) or (age<=25):
    
    amount = int(input ("Enter required loan amount : "))
    if (amount >= 50000):
        print ("Maximum loan amount is 50000")
    else :
        print ("You are eligible for loan")

else :
    print("You are not eligible for loan")
