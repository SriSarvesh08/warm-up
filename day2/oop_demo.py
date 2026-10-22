class BankAccount:
    def __init__(self, name, balance=0):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount

    def __str__(self):
        return f"{self.name}: Rs.{self.balance:.2f}"
if __name__ == "__main__":
    account = BankAccount("Sri Sarvesh", 2000)
    assert account.balance == 2000
    account.deposit(1000)
    assert account.balance == 3000
    account.withdraw(750)
    assert account.balance == 2250
    account.deposit(500)
    account.withdraw(250)
    assert account.balance == 2500
    try:
        account.withdraw(5000)
        assert False, "Insufficient balance validation failed"
    except ValueError:
        assert account.balance == 2500
    try:
        account.deposit(0)
        assert False, "Invalid deposit validation failed"
    except ValueError:
        assert account.balance == 2500
    try:
        BankAccount("", 1000)
        assert False, "Empty name validation failed"
    except ValueError:
        pass
    print(account)
    print("All 7 test checks passed!")