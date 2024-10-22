def main():
    cc = input("camelCase: ")
    print("snake_case: ", snake_case(cc), sep = "")




def snake_case(camelCase):
    for l in camelCase:
        if l.islower():
            print(l, end = "")
        if l.isupper():
            print("_", l.lower(), end = "", sep = "")



main()
