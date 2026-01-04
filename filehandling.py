

f=open("fruits.txt") # it will open in read mode (default)
print(f)
content=f.read()
print(content)
f.close() #always we should close file when we open

f=open("fruits.txt", "w") # it will open in write mode
print(f)
f.write("Hi\n")
f.write ("Bye\n") #write mode will erase the existing data 
f.close()

f=open("fruits.txt", "a") # it will open in append mode mode
print(f)
f.write("Apple\n")
f.write ("Orange\n") #Append mode will not erase the existing data 
f.close()


f=open("fruits.txt", "r+") # it will open in write & read mode mode
print(f)
print(f.read())
f.write("Apple\n")
f.write ("Orange\n")
print(f.read())
f.close()

f=open("fruits.txt", "r+") # it will open in write & read mode mode
print(f)

print(f.readline()) #it will read first line
f.close()
