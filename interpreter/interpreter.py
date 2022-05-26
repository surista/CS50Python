expression = input("Expression: ")
expression = expression.split(" ")
firstVar = int(expression[0])
operator = expression[1]
secondVar = int(expression[2])
if operator == "+":
    sol = firstVar + secondVar
elif operator == "-":
    sol =firstVar - secondVar
elif operator == "*":
    sol = firstVar * secondVar
else:
    sol = firstVar / secondVar

print("{:.1f}".format(sol))


