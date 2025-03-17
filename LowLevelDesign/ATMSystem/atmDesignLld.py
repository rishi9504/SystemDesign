# Designing an ATM System

# The ATM system should support basic withdrawal and deposit operations, as well as balance inquiry. It should also handle transactions with multiple accounts and multiple users.

# The system should be able to handle errors gracefully and provide appropriate error messages to the user.

# The system should be able to interact with bank backend to validate user accounts and perform transactions.

# The system should be able to handle concurrent access to accounts and transactions.

# ATM should be able to dispense bills and coins.

# The card should have a unique serial number and should be authenticated by the pin.

from abc import ABC, abstractmethod
class Card:
    def __init__(self, serial_number, pin):
        self.serial_number = serial_number
        self.pin = pin

    def authenticate(self, pin):
        return self.pin == pin
    
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount

# the transaction class is an abstract base class for different types of transactions. it is extended by withdrawltransaction and deposittransaction classes

class Transaction:
    def __init__(self,transaction_id, account, amount):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount

    @abstractmethod
    def execute(self):
        pass

class WithdrawalTransaction(Transaction):
    def execute(self):
        if self.account.withdraw(self.amount):
            print(f"Withdrew ${self.amount} from account {self.account.account_number}")
        else:
            print(f"Insufficient funds in account {self.account.account_number}")

class DepositTransaction(Transaction):
    def execute(self):
        self.account.deposit(self.amount)
        print(f"Deposited ${self.amount} into account {self.account.account_number}")

class CashDispenser:
    def dispense_cash(self, amount):
        print(f"Dispensing ${amount} in bills and coins")

class ATM:
    def __init__(self, card, cash_dispenser):
        self.card = card
        self.cash_dispenser = cash_dispenser
        self.transactions = []

    def process_transaction(self, transaction):
        transaction.execute()
        self.transactions.append(transaction)    
        self.cash_dispenser.dispense_cash(transaction.amount)

    def get_transactions(self):
        return self.transactions

    def get_balance(self, account):
        return account.balance

    def get_account(self, account_number):
        return Account(account_number, 0)

    def get_card(self):
        return self.card

    def get_pin(self):
        return self.card.pin

    def get_serial_number(self):
        return self.card.serial_number

    def authenticate(self, pin):
        return self.card.authenticate(pin)

    def get_transaction_id(self):
        return len(self.transactions)

if __name__ == "__main__":
    card = Card("1234567890", "1234")
    atm = ATM(card, CashDispenser())
    account = atm.get_account("12345")
    transaction = WithdrawalTransaction(atm.get_transaction_id(), account, 100)
    atm.process_transaction(transaction)
    print(atm.get_balance(account))
    transaction = DepositTransaction(atm.get_transaction_id(), account, 100)
    atm.process_transaction(transaction)
    print(atm.get_balance(account))
    print(atm.get_transactions())                