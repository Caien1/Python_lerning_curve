# when for loop use a copy to remove
backpack = ["Pizza","Pizza","Pizza","Pizza"]

for item in backpack:
    if item == "Pizza":
        backpack.remove(item)

print(backpack)

#use a copy because it doesnt shift the content after remove a new copy each time
backpack2 = ["Pizza","Pizza","Pizza","Pizza"]

for item in backpack2[:]:
    if item == "Pizza":
        backpack2.remove(item)
print(backpack2)