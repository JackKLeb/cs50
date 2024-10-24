def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x = [".", " "]
    if is_digit(s):
        return False
    if 2 <= len(s) <= 6:
        return True
    if x in s:
        return False

def is_digit(s):
    n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in s[0:2]:
        if i in n:
            return True
main()
