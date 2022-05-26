def main():
    user_input = input("What time is it? ")
    time = convert(user_input)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >=12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    time = time.strip().split(":")
    hours = int(time[0])
    minutes = int(time[1]) / 60
    return hours + minutes



if __name__ == "__main__":
    main()
