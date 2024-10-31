def main():
    while True:
        ratio = fuel()

        z = perc(ratio[0], ratio[-1])

        if z <= 1:
            print("E")
            break

        elif 1 < z < 98.5:
            print(f"{z:.0f}%")
            break

        elif 98.5 <= z <= 101:
            print("F")
            break

        else:
            continue

def fuel():
    while True:
        try:
            i = input("Fraction: ").strip().split("/")
            i = list(map(int, i))
            
            if i[0] > i[-1] or i[-1] == 0:
                continue

            if i[-1] == 0:
                raise ZeroDivisionError
            return i

        except (ValueError, ZeroDivisionError):
            pass


def perc(x, y):
    z = x / y * 100
    return z


main()
