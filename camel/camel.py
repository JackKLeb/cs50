cc = input("camelCase: ")
print ("snake_case: ", end = "")




for l in cc:
    if l.islower():
        print(l, end = "")
    else:
        print("_", l.lower(), end = "", sep = "")
print()

