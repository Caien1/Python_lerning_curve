backpack = ["guns","buns","lungs","guns","guns","guns"]

backpack[:] = [item for item in backpack if item != "guns"]
print(backpack)