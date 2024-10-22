def main():
    math = input("Expression: ").strip().split(" ")
    
    #print(math)

    x = float(math[0])
    y = math[1]
    z = float(math[2])

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    else:
        print(x / z)


main()
