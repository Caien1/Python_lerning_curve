workdays = ["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
workdays.append("Sunday")
print(workdays)
del workdays[-1]

del workdays[workdays.index("Saturday"):workdays.index("Saturday")+1]

print(workdays)