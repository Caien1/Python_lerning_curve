backpack = ["pizza","wine","pizza","brandy","martini","whiskey","pizza"]
backpack.remove("pizza") #returns None; removes first occurance only
print(backpack)

while backpack.count("pizza") > 0: # not proformant o=O(n**2)
    backpack.remove("pizza")

print(backpack)