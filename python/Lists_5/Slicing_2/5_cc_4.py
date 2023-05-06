backpack = ["pizza","wine","pizza","brandy","martini","whiskey","pizza"]

print(id(backpack))

backpack2=backpack # points to same location in memory

print(id(backpack2))

backpack3 = backpack[:] # different object a pure copy
print(id(backpack3))

backpack[:] = [1,2,3]
print(id(backpack))

backpack = [1,2,3]
print("new object",id(backpack))

