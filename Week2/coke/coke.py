
due = 50
due = int(due)
balance = 0


while balance <= 50:
    print("Amount due:", due)
    balance = input("Insert coins: ")
    balance = int(balance)
    #subtract the balance from the amount due
    due -= balance
    if due == 0:
        print("You have paid for a Coke!")
        break



