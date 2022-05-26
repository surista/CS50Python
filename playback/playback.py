input = input("Please enter your string: ")
newInput = input.split()
myString = ""
print(len(newInput))
for word in range(len(newInput)-1):
    newString = newInput[word] + "..."
    myString = myString + newString
myString += newInput[-1]
print(myString)