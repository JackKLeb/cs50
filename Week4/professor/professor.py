import random


def main():
    level = get_level()
    x_list, y_list = generate_integer(level)
    #print(x_list)
    #print(y_list)
    l, ls = generate_levels(x_list, y_list)
    #print(l)
    #print(ls)

#set all the variables
    i = 0
    score = 0
    chance = 0
    while i < 10:
        try:
            question = int(input(f"{l[i]} = "))
            #if the answer is correct add 1 to the score and move on the next quesiton
            if question == ls[i]:
                score += 1
                i += 1
                chance = 0
                continue
            else:
                raise ValueError
                #three chances to get the question correct, if not, move onto the next question
        except ValueError:
            print("EEE")
            chance += 1
            if chance < 3:
                continue
            else:
                print(f"{l[i]} = {ls[i]}")
                i += 1
                continue

    print(f"Score: {score}")

#ask for a level
def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 0 < level and level < 4:
                break
            else:
                raise ValueError
        except ValueError:
            continue
    return level

#generate 2 lists of ten numbers with the same # of digits as the level #
def generate_integer(level):
    x_list = []
    y_list = []
    i = 0

    if level == 1:
        while i < 10:
            x = random.randint(0,9)
            x_list.append(x)

            y = random.randint(0,9)
            y_list.append(y)
            i += 1
        return x_list, y_list

    elif level == 2:
        while i < 10:
            x = random.randint(10,99)
            x_list.append(x)

            y = random.randint(10,99)
            y_list.append(y)
            i += 1
        return x_list, y_list

    else:
        while i < 10:
            x = random.randint(100,999)
            x_list.append(x)

            y = random.randint(100,999)
            y_list.append(y)
            i += 1

        return x_list, y_list

#generate 10 levels with solutions
def generate_levels(x, y):
    l = []
    ls = []
    i = 0

    while i < 10:
        lvl = (f"{x[i]} + {y[i]}")
        l.append(lvl)
        lvls = x[i] + y[i]
        ls.append(lvls)
        i += 1
    return l, ls

if __name__ == "__main__":
    main()
