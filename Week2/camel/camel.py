def main():
    cc = input("camelCase: ")
    print(snake_case(cc))




def snake_case(camelCase):
    for i in camelCase:
        if i.islower():
            print(i, end = "")
        if i.isupper():
            print("_", i.lower(), end = "", sep = "")



main()
