def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    seenDigit = False
    if len(s) > 6 or len(s) < 2 or s[0].isdigit() or s[1].isdigit():
        return False

    for char in s:
        if char.isspace() or not char.isalnum():
            return False
        elif char.isdecimal():
                if not seenDigit and char == "0":
                    return False
                elif seenDigit and char.isalpha():
                    return False
                else:
                    seenDigit = True
        if char.isalpha() and seenDigit:
            return False
    return True

main()
