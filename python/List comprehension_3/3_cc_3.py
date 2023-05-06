healthy = ["kale chips","broccoli"]
backpack = ["pizza", "frozen custurd","apple crisp", "kale chips"]

healthy_backpack =[]


for item in backpack:
    if item in healthy:
        healthy_backpack.append(item)

print( healthy_backpack) 