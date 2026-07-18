class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} USD deposited. Current balance = {self.balance} USD")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Insufficient funds! Your current balance = {self.balance} USD")
        self.balance -= amount
        print(f"{amount} USD withdrawn. Current balance = {self.balance} USD")


# Initialize the account with 0 balance
account = BankAccount(0)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Your choice = ").strip()

    if choice == "1":
        print(f"Current Balance = {account.balance} USD")
    elif choice == "2":
        amount = int(input("Enter amount to deposit = "))
        account.deposit(amount)
    elif choice == "3":
        amount = int(input("Enter amount to withdraw = "))
        try:
            account.withdraw(amount)
        except ValueError as error:
            print(error)
    elif choice == "4":
        print("Closing...")
        break

# 'self' represents the instance of the class itself in Python.