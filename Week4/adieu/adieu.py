#Tried this method below and it works but the check50 didn't like it, not sure why.

"""
def main():
    names = []


    while True:
        try:
            name = input("Name: ").strip().title()
            names.append(name)
        #Stop asking for names after a ctrl+D
        except EOFError:
            if len(names) > 1:
                full = adieu(names)
                print()
                print(f"Adieu, adieu, to {full}")
                break
            else:
                print()
                print(f"Adieu, adieu, to {names[0]}")
                break
#format the names
def adieu(i):

    comma = i[:-1]
    comma_list = []
    #add a comma after each name
    for n in comma:
        n = f"{n},"
        comma_list.append(n)

    full = " ".join(comma_list)
    rest = f"and {i[-1]}"
    full = f"{full} {rest}"
    return full

main()
"""

#Checked the hint and used the inflect library instead, much easier
import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip().title()
        names.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(names))
        break
