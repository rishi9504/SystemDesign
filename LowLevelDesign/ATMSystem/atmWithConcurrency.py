import threading
import time

# Simulated Bank Database
BANK_ACCOUNTS = {
    "123456": {"pin": "1234", "balance": 1000},
    "654321": {"pin": "4321", "balance": 500}
}
LOCK = threading.Lock()

class ATM:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.is_authenticated = self.authenticate_user()

    def authenticate_user(self):
        if self.card_number in BANK_ACCOUNTS and BANK_ACCOUNTS[self.card_number]["pin"] == self.pin:
            print("Authentication Successful.")
            return True
        else:
            print("Authentication Failed.")
            return False

    def check_balance(self):
        if not self.is_authenticated:
            print("Unauthorized access.")
            return
        with LOCK:
            balance = BANK_ACCOUNTS[self.card_number]["balance"]
        print(f"Your current balance is: ${balance}")

    def deposit(self, amount):
        if not self.is_authenticated:
            print("Unauthorized access.")
            return
        with LOCK:
            BANK_ACCOUNTS[self.card_number]["balance"] += amount
        print(f"Successfully deposited ${amount}. New balance: ${BANK_ACCOUNTS[self.card_number]['balance']}")

    def withdraw(self, amount):
        if not self.is_authenticated:
            print("Unauthorized access.")
            return
        with LOCK:
            if BANK_ACCOUNTS[self.card_number]["balance"] >= amount:
                BANK_ACCOUNTS[self.card_number]["balance"] -= amount
                print(f"Dispensing ${amount}. New balance: ${BANK_ACCOUNTS[self.card_number]['balance']}")
            else:
                print("Insufficient funds.")

# Simulate multiple users accessing the ATM

def user_session(card_number, pin, action, amount=0):
    atm = ATM(card_number, pin)
    if not atm.is_authenticated:
        return

    if action == "balance":
        atm.check_balance()
    elif action == "deposit":
        atm.deposit(amount)
    elif action == "withdraw":
        atm.withdraw(amount)

if __name__ == "__main__":
    users = [
        threading.Thread(target=user_session, args=("123456", "1234", "balance")),
        threading.Thread(target=user_session, args=("123456", "1234", "deposit", 200)),
        threading.Thread(target=user_session, args=("123456", "1234", "withdraw", 100)),
        threading.Thread(target=user_session, args=("654321", "4321", "withdraw", 600)),
    ]

    for user in users:
        user.start()
    for user in users:
        user.join()

    print("\nFinal Bank Account State:", BANK_ACCOUNTS)
