class goa:

    name=""
    drink=""
    def party(self):
        print("Lets Party......")
    def beach(self):
        print("Enjoying the becah")

ramesh = goa()
suresh = goa()

ramesh.name = "Ramesh"
suresh.name = "Suresh"

ramesh.drink = "yes"
suresh.drink = "No"


print(ramesh.name)
print("Drink : ",ramesh.drink)
ramesh.party()

print(suresh.name)
print("Drink : ",suresh.drink)
suresh.beach()
