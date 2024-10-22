def main():

    #cc = input("camelCase: ")
    print ("snake_case: ", end = "")

def sc(l):
    cc = input("camelCase: ")
    for l in cc:
        if l.islower():
            print(l, end = "")
        else:
            print("_", l.lower(), end = "", sep = "")




main()
"""
for l in cc:
    if l.islower():
        print(l, end = "")
    else:
        print("_", l.lower(), end = "", sep = "")
print()
"""
