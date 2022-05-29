
def show_fraction():
    valid = False
    while not valid:
        try:
            prompt = input("Fraction: ")
            prompt = prompt.split("/")
            fraction = int(prompt[0]) / int(prompt[1])
            if int(prompt[0]) > int(prompt[1]):
                pass
            else:
                valid = True
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    if (fraction <= 0.01):
        print("E")
    elif fraction >= 0.99:
        print("F")
    else:
        print(f"{fraction:.0%}")


show_fraction()