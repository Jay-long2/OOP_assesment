class BankAccount():
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        if amount<0:
            print("Insufficent funds to deposit")
        else:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self,amount):
        if amount < 0:
            print("Insufficient funds to withdraw")
        else:
            self.balance -= amount
            print(f"withdrew: {amount}.New balance: {self.balance}")
    def get_balance(self):
        """Return the current balance (read-only access)."""
        return self.balance

account = BankAccount(100)  # Creating an account with an initial balance of $100

# Depositing money
account.deposit(50)

# Withdrawing money
account.withdraw(30)


    

