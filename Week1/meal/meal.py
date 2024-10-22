def main():
    #ask question
    meal = input("What time is it? ").strip()

    #check if it is meal time

    if 7.0 <= convert(meal) <= 8:
        print("breakfast time")
    elif 12.0 <= convert(meal) <= 13:
        print("lunch time")
    elif 18 <= convert(meal) <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    x, y = time.split(":")
    hr = float(x)
    min = float(y) / 60
    time = hr + min
    return time


if __name__ == "__main__":
    main()

