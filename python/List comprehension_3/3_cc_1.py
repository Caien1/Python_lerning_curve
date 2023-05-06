healthy = ["kale chips","broccoli"]
backpack = ["pizza", "frozen custurd","apple crisp", "kale chips"]

print(id(backpack))
backpack = [item for item in backpack if item in healthy]
print(backpack)
print(id(backpack))

