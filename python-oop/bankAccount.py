


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
     def __init__(self, account_holder, initial_balance=0, interest_rate=0.02):
          super().__init__(account_holder, initial_balance)
          self.interest_rate = interest_rate
     
     def apply_interest(self):
          interest = self.balance * self.interest_rate
          self.deposit(interest)
          print(f"Applied interest: ${interest:.2f}")
     
     def __str__(self):
          return (f"Savings Account Holder: {self.account_holder}, "
                    f"Balance: ${self.balance:.2f}, "
                    f"Interest Rate: {self.interest_rate * 100:.2f}%")
     
if __name__ == "__main__":
     # Example usage
     account = BankAccount("John Doe", 1000)
     print(account)
     account.deposit(500)
     account.withdraw(200)
     print(f"Current Balance: ${account.get_balance():.2f}")
     
     savings = SavingsAccount("Jane Doe", 2000, 0.03)
     print(savings)
     savings.apply_interest()
     print(f"Current Balance after interest: ${savings.get_balance():.2f}")