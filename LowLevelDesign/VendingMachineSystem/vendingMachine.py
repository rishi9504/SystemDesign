from enum import Enum
from threading import Lock
import uuid

# Enum for Product Types
class ProductType(Enum):
    SNACK = "Snack"
    DRINK = "Drink"
    CANDY = "Candy"

# Product Class
class Product:
    def __init__(self, product_id, name, price, quantity, product_type):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_type = product_type

    def is_available(self):
        return self.quantity > 0

    def dispense(self):
        if self.is_available():
            self.quantity -= 1
            return True
        return False

# Vending Machine Class
class VendingMachine:
    def __init__(self):
        self.products = {}
        self.balance = 0.0
        self.lock = Lock()

    def add_product(self, name, price, quantity, product_type):
        product_id = str(uuid.uuid4())
        self.products[product_id] = Product(product_id, name, price, quantity, product_type)
        return product_id

    def insert_money(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Current Balance: ${self.balance}")

    def select_product(self, product_id):
        with self.lock:
            if product_id not in self.products:
                print("Invalid Product Selection")
                return False

            product = self.products[product_id]
            if not product.is_available():
                print("Product is out of stock.")
                return False

            if self.balance < product.price:
                print("Insufficient funds.")
                return False

            product.dispense()
            self.balance -= product.price
            change = self.balance
            self.balance = 0.0  # Reset balance after purchase
            print(f"Dispensing {product.name}. Change: ${change:.2f}")
            return True

    def restock_product(self, product_id, quantity):
        with self.lock:
            if product_id in self.products:
                self.products[product_id].quantity += quantity
                print(f"Restocked {self.products[product_id].name}. New Quantity: {self.products[product_id].quantity}")

    def collect_money(self):
        with self.lock:
            collected_amount = self.balance
            self.balance = 0.0
            print(f"Collected ${collected_amount} from the machine.")

# Simulation
if __name__ == "__main__":
    vending_machine = VendingMachine()
    
    # Add products
    snack_id = vending_machine.add_product("Chips", 1.50, 10, ProductType.SNACK)
    drink_id = vending_machine.add_product("Soda", 2.00, 5, ProductType.DRINK)
    
    # User inserts money and purchases a product
    vending_machine.insert_money(2.00)
    vending_machine.select_product(snack_id)
    
    # Restock and collect money
    vending_machine.restock_product(snack_id, 5)
    vending_machine.collect_money()
from collections import defaultdict