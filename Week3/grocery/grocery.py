def main():

    list = []

    while True:
        try:

            item = input().upper()
            list.append(item)

        except EOFError:
            break

    list.sort()

    for item in sorted(set(list)):

        amount = list.count(item)
        print(amount, item)

main()
