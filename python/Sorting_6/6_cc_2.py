strings = ["a","A","abc","ABC","aBc","Abc"]

strings.sort()
print(strings)
strings.sort(key=str.lower)
print(strings)
