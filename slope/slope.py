def main():
    #y = mx + b
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    b = int(input("y-intersept: "))

    y = y2 - y1
    x = x2 - x1
    m = x / y

    print("Slope:", m)

    print("Your Line: y = ", m, "x + ", b, sep = "")







main()
