#if dublicate data id not needed and order doesnt matter
backpack = {"Sword","Sword","sword","pizza","gun"}
print(backpack)
backpack.add("test")
print(backpack)
print("sword"in backpack)
#implimented as a hash O(1) average insert/update/delete O(len(s))