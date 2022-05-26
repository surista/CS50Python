user_input = input("camelCase: ")
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(user_input)):
    if user_input[i] in upper_case:
        first_part = user_input[0:i]
        second_part = user_input[i:].lower()

print(first_part + "_" + second_part)

