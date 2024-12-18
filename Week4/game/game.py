import random
import sys

def main():
    while True:
        #check if number is int
        try:
            n = int(input("Level: "))
            #check if number is positive
            if n > 0:
                break
            else:
                continue

        except (ValueError, EOFError):
            continue

    x = random.randint(1, n)

    #asks for a guess and outputs the respective answer
    while True:
        try:
            g = int(input("Guess: "))
            if g > 0:
                c = check(g, x)
                if len(c) == 11:
                    print(c)
                    break
                else:
                    print(c)
                    continue
            else:
                continue

        except (ValueError, EOFError):
            continue
    sys.exit()

def check(g, x):
    if g == x:
        a = "Just right!" #len 11
        return a
    elif g > x:
        a = "Too large!" #len 10
        return a
    else:
        a = "Too small!" #len 10
        return a

main()
