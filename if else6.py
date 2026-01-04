
a = int(input ("Enter Num1 : "))
b = int(input ("Enter Num2 : "))
operation = input("add/sub/mul/div : ")

if (operation == "add") :
    print ("Addition of",a, "and",b,"is : ",a+b)
elif (operation == "sub") :
    print ("subtraction of",a, "and",b,"is : ",a-b)
elif (operation == "mul") :
    print ("Multiplication of",a, "and",b,"is : ",a*b)
elif (operation == "div") :
    print ("Division of",a, "and",b,"is : ",a/b)
else :
    print ("Invalid operation")
