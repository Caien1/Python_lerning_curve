data = [1,2,3,4,5]
print(id(data))
data[:]=data[::-1]
print(id(data))
print(data)