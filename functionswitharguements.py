
a=int(input("Enter Number "))

def findevenorodd(num):
    """if we pass a=10 throgh func only that value will be passed here, now this num will have value of a i.e is 10 """
    if(num%2==0):
        print(num," is even number")
    else:
        print(num, " is odd number")

findevenorodd(a)
