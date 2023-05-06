data = [1,3,4,6,2,6,8,9]
index = 0
while index<len(data)/2:#O(n/2)
    data[index], data[-index-1]= data[-index-1],data[index]
    index+=1

print(data)
index =0
for index in range(len(data)//2):
        data[index], data[-index-1]= data[-index-1],data[index]
print(data)