def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:1].isdigit:
        return False
    if 2 <= len(s) <= 6:
        return True

def is_digit(s):
    for l in s[0:1]:
        if l == range(10)
main()
