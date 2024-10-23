
def main():

    In = input("Input: ")

    for l in In:
        if isvowel(l):
            print("", end = "", sep = "")
        else:
            print(l, end = "", sep = "")



def isvowel(letter):
    if letter.lower() in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False


main()
