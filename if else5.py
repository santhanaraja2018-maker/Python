

score = int(input("Enter your score : "))

if (score < 35):
    print ("Poor Student")
elif (score >= 35 and score <= 70):
    print ("Averge Student")
elif (score > 70 and score <= 100):
    print ("Good Student")
else:
    print("Invalid Number")
