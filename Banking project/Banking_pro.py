def show_balance(balance):
    print(f"Your balance is {balance:.2f} cr")
    print(".......................................................")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    print(".......................................................")

    if amount <= 0:
        print("That's not a valid amount.")
        print(".......................................................")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds.")
        print(".......................................................")
        return 0
    elif amount < 200:
        print("The amount must be a minimum of 200.")
        print(".......................................................")
        return 0
    elif amount <= 0:
        print("Amount must be positive.")
        print(".......................................................")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print(".......................................................")

    choice = input("Enter a number (1-4): ")
    if choice == '1':
        show_balance(balance)
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw(balance)
    elif choice == '4':
        is_running = False
    else:
        print("That is not a valid choice.")
        print(".......................................................")

print("Thank You! Have a nice day.")
