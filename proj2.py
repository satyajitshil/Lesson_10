string = input("Type a word, name or phrase:")

string2 = ('')
for i in string:
    string2 = i + string2

print("Regular string =",string)
print("Reverse string =",string2)