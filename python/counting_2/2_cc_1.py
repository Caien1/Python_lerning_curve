backpack =["guns","rubber duck","slice of pizza","parachute","guns", "guns"]

count = [[backpack.count(items),items] for items in set(backpack)] # random order each time
print(count)

[print(backpack.count(items),items) for items in set(backpack)]