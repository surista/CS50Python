user_input = input("camelCase: ")

def convertToSnakeCase(user_input):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sol = ""
    for char in user_input:
        if char in upper_case:
            sol = sol + "_" + char.lower()
        else:
            sol = sol + char
    return sol

print(convertToSnakeCase(user_input))


