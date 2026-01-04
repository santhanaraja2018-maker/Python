

s_username="EMC"
s_password="123"

username = input("Enter your name ")
password = input("Enter password ")


def validate():
    if (s_username == username and s_password == password):
        return True
    else :
        return False

a=validate()
print(a)
