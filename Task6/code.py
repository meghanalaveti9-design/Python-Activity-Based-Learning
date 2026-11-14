balance = 5000.0
transactions = []

while True:
    print("\nATM MENU")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Transaction summary")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Deposit amount: Rs. "))
        if amount > 0:
            balance += amount
            transactions.append(("Deposit", amount))
            print("Deposit successful.")
        else:
            print("Amount must be positive.")
    elif choice == "2":
        amount = float(input("Withdrawal amount: Rs. "))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > 20000:
            print("Withdrawal exceeds the single-transaction limit.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful.")
    elif choice == "3":
        print("Current balance: Rs.", round(balance, 2))
    elif choice == "4":
        print("TRANSACTION SUMMARY")
        if not transactions:
            print("No transactions yet.")
        for kind, amount in transactions:
            print(kind, ": Rs.", amount)
        print("Current balance: Rs.", round(balance, 2))
    elif choice == "5":
        print("Thank you for using the ATM simulation.")
        break
    else:
        print("Invalid option. Choose 1 to 5.")
