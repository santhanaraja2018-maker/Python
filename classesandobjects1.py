

class laptop:
    price=0
    processor=""
    ram=""

Hp = laptop()
Dell = laptop()
Lenovo = laptop()

Hp.price = 40000
Hp.processor="i5"
Hp.ram = "8GB"


Dell.price = 50000
Dell.processor="i7"
Dell.ram = "16GB"


print("HP")
print(Hp.price)
print(Hp.processor)
print(Hp.ram)

print("DELL")
print(Dell.price)
print(Dell.processor)
print(Dell.ram)
