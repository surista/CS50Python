menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
    }

total = 0
try:
    while True:
        prompt = input("Item: ")
        prompt = prompt.lower()
        if prompt in menu:
            total = total + menu[prompt]
            print(f"Total: ${total:.2f}")
except EOFError:
    pass

print(f"Total: ${total:.2f}")


