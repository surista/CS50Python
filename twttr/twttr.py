user_input = input("Input: ")
sol = ""
vowels = "aeiouAEIOU"
for char in user_input:
    if char in vowels:
        sol = sol + ""
    else:
        sol = sol + char

print(sol)

