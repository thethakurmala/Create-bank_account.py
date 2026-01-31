"""
TASK 10: Object-Oriented Programming (OOP)
Bank Account Simulation
"""

class BankAccount:
    """Base class for bank account"""

    def __init__(self, account_holder, balance=0):
        # Encapsulation: protected attribute
        self._account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self._balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        """Return current balance"""
        return self._balance


# Inheritance
class SavingsAccount(BankAccount):
    """Derived class from BankAccount"""

    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    # Method overriding (Polymorphism)
    def get_balance(self):
        interest = self._balance * self.interest_rate
        total = self._balance + interest
        print(f"Balance with interest: ₹{total}")
        return total


# Creating objects
print("---- Bank Account Demo ----")

account1 = BankAccount("Rahul", 1000)
account1.deposit(500)
account1.withdraw(300)
print("Final Balance:", account1.get_balance())

print("\n---- Savings Account Demo ----")

account2 = SavingsAccount("Neha", 2000)
account2.deposit(1000)
account2.get_balance()
