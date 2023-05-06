data = [1,2,3,4,5]
data.reverse() # returns None
print(data)

size = len(data)-1
data2=[]
while size>-1:
    data2.append(data[size])
    size = size-1

print(data2)

for item in reversed(data):
    data2[:].append(item)

print(data2)