class BankAccount:
    def __init__(self, name, account_no, ifsc_code, balance=0):
        self.name = name
        self.account_no = account_no
        self.ifsc_code = ifsc_code
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        else:
            return "INVALID amount deposited."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount}. New balance: {self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def balance_enquiry(self):
        return f"Account holder: {self.name}\nAccount No: {self.account_no}\nIFSC Code: {self.ifsc_code}\nBalance: {self.balance}"


# Test
bank = BankAccount("Shiva", "389057395887", "Noo1234", 100)
print(bank.balance_enquiry())
print(bank.deposit(1000))
print(bank.withdraw(1000))
print(bank.balance_enquiry())
