class shape():
    def area(self):
        return 0
class rectangle(shape):

    #method overriding
    def area(self):
        l=10
        b=20
        print(l*b)

r1=rectangle()
r1.area()
