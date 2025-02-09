This repository contains resources to learn Low Level Design (LLD) / Object Oriented Design (OOD) and prepare for interviews.

Updating this repo inspired by this Awesome Low Level Design Repo (Github Link) [https://github.com/ashishps1/awesome-low-level-design]


Basics OOP Concepts


In an LLD interview, you should aim to explain Object-Oriented Programming (OOP) concepts in a structured manner with clear examples. 

---

### **Object-Oriented Programming (OOP) in Python**
OOP is a programming paradigm that organizes code into objects, making it modular, reusable, and scalable. Python supports four key OOP principles:

### **1. Encapsulation**
   - **Definition:** Wrapping data (variables) and methods (functions) inside a class while restricting direct access to some components.
   - **Purpose:** Protects the integrity of data by preventing unintended modifications.
   - **Implementation in Python:**
     - Use **private (`__`) and protected (`_`) attributes**.
     - Provide getter and setter methods.

   ```python
   class BankAccount:
       def __init__(self, account_number, balance):
           self.account_number = account_number  # Public
           self.__balance = balance  # Private

       def deposit(self, amount):
           if amount > 0:
               self.__balance += amount

       def get_balance(self):
           return self.__balance  # Access through method

   account = BankAccount("12345", 1000)
   print(account.get_balance())  # ✅ Works
   print(account.__balance)  # ❌ AttributeError (private variable)
   ```

---

### **2. Abstraction**
   - **Definition:** Hiding implementation details and exposing only necessary functionality.
   - **Purpose:** Reduces complexity and increases code maintainability.
   - **Implementation in Python:**
     - Use **abstract classes and methods** (via `ABC` module).

   ```python
   from abc import ABC, abstractmethod

   class Payment(ABC):
       @abstractmethod
       def process_payment(self, amount):
           pass  # Abstract method

   class CreditCardPayment(Payment):
       def process_payment(self, amount):
           print(f"Processing credit card payment of ${amount}")

   payment = CreditCardPayment()
   payment.process_payment(100)  # ✅ Works
   ```

---

### **3. Inheritance**
   - **Definition:** A mechanism where a child class derives properties and behavior from a parent class.
   - **Purpose:** Promotes code reusability and establishes relationships between classes.
   - **Implementation in Python:**
     - Use `class ChildClass(ParentClass)`.
     - Override parent methods if needed.

   ```python
   class Animal:
       def speak(self):
           return "Some sound"

   class Dog(Animal):
       def speak(self):
           return "Bark"

   dog = Dog()
   print(dog.speak())  # Output: Bark
   ```

---

### **4. Polymorphism**
   - **Definition:** The ability of different classes to be treated as instances of the same parent class, with method overriding or operator overloading.
   - **Purpose:** Enables flexibility in calling methods without knowing the exact object type.
   - **Implementation in Python:**
     - **Method Overriding** (Child class redefines a method from Parent).
     - **Operator Overloading** (`__add__`, `__str__`, etc.).

   ```python
   class Bird:
       def fly(self):
           return "Flying"

   class Sparrow(Bird):
       def fly(self):
           return "Sparrow flying low"

   class Eagle(Bird):
       def fly(self):
           return "Eagle flying high"

   def make_it_fly(bird):
       print(bird.fly())

   make_it_fly(Sparrow())  # Output: Sparrow flying low
   make_it_fly(Eagle())    # Output: Eagle flying high
   ```

---

1. **Encapsulation** → Hides data using private/protected attributes.
2. **Abstraction** → Hides implementation details via abstract classes.
3. **Inheritance** → Enables code reuse and establishes relationships.
4. **Polymorphism** → Allows multiple classes to have the same interface.

### **Real-World Applications of OOP Concepts in Python**  


---

### **1. Encapsulation → Data Security in Banking Systems**  
- **Use Case:** Protect sensitive user data in a banking application.  
- **Example:** A `BankAccount` class restricts direct access to the account balance and provides methods for deposits and withdrawals.

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        return "Insufficient funds"

    def get_balance(self):
        return self.__balance  # Safe access

# Usage
account = BankAccount("12345", 1000)
account.deposit(500)
print(account.get_balance())  # ✅ 1500
print(account.__balance)  # ❌ AttributeError (can't access private variable)
```
- **Why?** Prevents unauthorized access to balance, ensuring security.

---

### **2. Abstraction → Payment Gateway System (PayPal, Stripe, Razorpay, etc.)**  
- **Use Case:** A payment gateway should support different payment methods (Credit Card, PayPal, UPI, etc.) but expose a common interface.  
- **Example:** Abstract class `Payment` ensures all payment methods follow a uniform structure.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass  # Defined in child classes

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class UpiPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount}")

# Usage
def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

make_payment(CreditCardPayment(), 200)  # ✅ Works with CreditCard
make_payment(UpiPayment(), 100)         # ✅ Works with UPI
```
- **Why?** Abstraction ensures **new payment methods** can be added **without modifying existing code**.

---

### **3. Inheritance → User Management in Web Apps (Admin vs. Regular User)**  
- **Use Case:** In a web app, **Admins** have additional privileges over **Regular Users** (e.g., modifying user data).  
- **Example:** The `AdminUser` class inherits from `User`, reusing common properties and adding extra privileges.

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_details(self):
        return f"User: {self.username}, Email: {self.email}"

class AdminUser(User):  # Inherits from User
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)  # Reuse Parent class attributes
        self.admin_level = admin_level

    def delete_user(self, user):
        return f"Admin {self.username} deleted user {user.username}"

# Usage
user = User("john_doe", "john@example.com")
admin = AdminUser("admin123", "admin@example.com", "Super")

print(user.get_details())  # ✅ User: john_doe, Email: john@example.com
print(admin.get_details())  # ✅ User: admin123, Email: admin@example.com
print(admin.delete_user(user))  # ✅ Admin admin123 deleted user john_doe
```
- **Why?** Promotes **code reusability** by eliminating redundancy in user role definitions.

---

### **4. Polymorphism → Strategy Pattern in Logging Frameworks**  
- **Use Case:** Logging frameworks like Python’s `logging` module allow different logging strategies (Console, File, Database).  
- **Example:** The `Logger` interface supports multiple output types.

```python
class Logger:
    def log(self, message):
        pass  # To be implemented in subclasses

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console Log: {message}")

class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(f"File Log: {message}\n")

# Usage
def log_message(logger, message):
    logger.log(message)

log_message(ConsoleLogger(), "System started")  # ✅ Console Log: System started
log_message(FileLogger(), "File saved")         # ✅ Saves "File saved" to log.txt
```
- **Why?** This allows the logging mechanism to be easily extended **without modifying existing code**.

---

### **Key Takeaways for Interviews**
| **OOP Concept** | **Real-World Use Case** | **Purpose** |
|---------------|-----------------|----------|
| **Encapsulation** | Banking systems (protecting account balance) | Data security |
| **Abstraction** | Payment gateways (hiding implementation details) | Simplifies API usage |
| **Inheritance** | User roles (Admin vs. Regular User) | Code reusability |
| **Polymorphism** | Logging frameworks (Console, File, Database loggers) | Flexible implementations |



[SOLID Principles with Pictures](https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898)



### **SOLID Principles in Python (LLD Interview-Ready Explanation)**
In **Low-Level Design (LLD) interviews**, SOLID principles help you **write maintainable, scalable, and flexible code**. These principles ensure better software design and **avoid common pitfalls like tight coupling and code duplication**.

---

## **1. Single Responsibility Principle (SRP)**
📌 **Definition:** A class should have **only one reason to change**—it should do **only one thing**.

📌 **Problem:** A `Report` class handles **both** report generation **and** file storage.

❌ **Bad Code (Violates SRP)**
```python
class Report:
    def __init__(self, content):
        self.content = content

    def generate(self):
        return f"Report Content: {self.content}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.content)  # ❌ Unrelated responsibility (File handling)
```
💡 **Fix:** **Separate concerns** into `Report` (business logic) and `FileManager` (file handling).

✅ **Good Code (Follows SRP)**
```python
class Report:
    def __init__(self, content):
        self.content = content

    def generate(self):
        return f"Report Content: {self.content}"

class FileManager:
    @staticmethod
    def save_to_file(filename, content):
        with open(filename, "w") as f:
            f.write(content)

# Usage
report = Report("Monthly Sales Data")
FileManager.save_to_file("report.txt", report.generate())
```
🎯 **Why?**  
- If file storage logic changes (e.g., switch to **cloud storage**), only `FileManager` is modified.
- Report generation remains **unaffected**, improving **maintainability**.

---

## **2. Open/Closed Principle (OCP)**
📌 **Definition:** Classes should be **open for extension** but **closed for modification**.

📌 **Problem:** A `Discount` class applies discounts **only for premium users**. Adding a **new discount type** requires modifying existing code.

❌ **Bad Code (Violates OCP)**
```python
class Discount:
    def apply_discount(self, price, user_type):
        if user_type == "premium":
            return price * 0.9  # ❌ Hardcoded logic
        return price
```
💡 **Fix:** Use **inheritance (or strategy pattern)** to allow new discounts **without modifying** the existing class.

✅ **Good Code (Follows OCP)**
```python
class Discount:
    def apply_discount(self, price):
        return price  # Default (No Discount)

class PremiumDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.9  # 10% off for premium users

class StudentDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.85  # 15% off for students

# Usage
def calculate_price(price, discount: Discount):
    return discount.apply_discount(price)

print(calculate_price(100, PremiumDiscount()))  # ✅ 90
print(calculate_price(100, StudentDiscount()))  # ✅ 85
```
🎯 **Why?**  
- New discount types can be **added as separate classes**, without modifying the `Discount` class.
- **Extensible design**—follows **OCP**.

---

## **3. Liskov Substitution Principle (LSP)**
📌 **Definition:** A child class should be **fully substitutable** for its parent **without breaking functionality**.

📌 **Problem:** A `Rectangle` class works fine, but its subclass `Square` **violates expectations** by overriding behavior incorrectly.

❌ **Bad Code (Violates LSP)**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):  # ❌ Inherits incorrectly
    def __init__(self, side):
        super().__init__(side, side)  # ❌ Forces width = height
```
💡 **Fix:** Instead of forcing `Square` to inherit from `Rectangle`, create a **separate base class**.

✅ **Good Code (Follows LSP)**
```python
class Shape:
    def area(self):
        pass  # Abstract method

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Usage
shapes = [Rectangle(4, 5), Square(4)]
for shape in shapes:
    print(shape.area())  # ✅ Works correctly for both
```
🎯 **Why?**  
- **Prevents unexpected behavior** when substituting `Square` for `Rectangle`.
- Each shape **defines its own area calculation**.

---

## **4. Interface Segregation Principle (ISP)**
📌 **Definition:** Clients should **not be forced to implement** methods they **don’t use**.

📌 **Problem:** A single `Worker` interface forces **all workers** to implement `eat()` even if they don’t eat (e.g., `Robot`).

❌ **Bad Code (Violates ISP)**
```python
class Worker:
    def work(self):
        pass

    def eat(self):
        pass  # ❌ Robots don't eat

class HumanWorker(Worker):
    def work(self):
        return "Working..."

    def eat(self):
        return "Eating lunch"

class RobotWorker(Worker):
    def work(self):
        return "Working..."

    def eat(self):
        raise NotImplementedError("Robots don't eat")  # ❌ Bad design
```
💡 **Fix:** Split interfaces into **Workable** and **Eatable**.

✅ **Good Code (Follows ISP)**
```python
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        return "Working..."

    def eat(self):
        return "Eating lunch"

class RobotWorker(Workable):
    def work(self):
        return "Working..."

# Usage
human = HumanWorker()
robot = RobotWorker()

print(human.work())  # ✅ Working...
print(human.eat())   # ✅ Eating lunch
print(robot.work())  # ✅ Working...
```
🎯 **Why?**  
- **Avoids forcing classes** to implement unnecessary methods.
- **Decouples responsibilities**, making code **modular**.

---

## **5. Dependency Inversion Principle (DIP)**
📌 **Definition:** High-level modules **should not depend on** low-level modules; both should depend on **abstractions**.

📌 **Problem:** A `UserService` class **directly depends on** `MySQLDatabase`. If we switch to **PostgreSQL**, we must modify `UserService`.

❌ **Bad Code (Violates DIP)**
```python
class MySQLDatabase:
    def connect(self):
        return "Connecting to MySQL"

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # ❌ Hard dependency

    def get_users(self):
        return self.db.connect()
```
💡 **Fix:** Use **abstraction (interface)** so `UserService` depends on **a generic database interface**.

✅ **Good Code (Follows DIP)**
```python
class Database:
    def connect(self):
        pass  # Abstract method

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connecting to PostgreSQL"

class UserService:
    def __init__(self, db: Database):
        self.db = db

    def get_users(self):
        return self.db.connect()

# Usage
mysql_service = UserService(MySQLDatabase())
postgres_service = UserService(PostgreSQLDatabase())

print(mysql_service.get_users())  # ✅ Connecting to MySQL
print(postgres_service.get_users())  # ✅ Connecting to PostgreSQL
```
🎯 **Why?**  
- **Easily switch databases** without modifying `UserService`.
- **Loose coupling → Better maintainability**.

---

| **SOLID Principle** | **Problem It Solves** | **Applied Design Pattern** |
|---------------------|---------------------|------------------|
| **SRP** | Avoids multiple responsibilities in a single class | Separation of Concerns |
| **OCP** | Avoids modifying existing code for new features | Strategy Pattern |
| **LSP** | Ensures child classes behave correctly when substituted | Subtyping |
| **ISP** | Avoids forcing unnecessary methods on classes | Interface Segregation |
| **DIP** | Reduces tight coupling between modules | Dependency Injection |


### **DRY (Don't Repeat Yourself) Principle in Python**  
📌 **Definition:**  
The **DRY principle** states that **"Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."**  
In simple terms, **avoid code duplication** by using **functions, classes, inheritance, and abstraction**.

📌 **Why is DRY important?**  
- **Reduces code duplication** → Less maintenance effort  
- **Improves readability** → Code is easier to understand  
- **Enhances reusability** → Promotes modularity  
- **Prevents inconsistencies** → No redundant logic to update  

---

## **❌ Bad Code (Violates DRY)**
Let's say we need to **calculate a discount** for both **regular customers and premium customers**.

```python
class RegularCustomer:
    def get_discounted_price(self, price):
        discounted_price = price - (price * 0.05)  # 5% discount
        return discounted_price

class PremiumCustomer:
    def get_discounted_price(self, price):
        discounted_price = price - (price * 0.10)  # 10% discount
        return discounted_price
```
### **🛑 What's wrong?**
- **Code duplication**: The logic for calculating the discount is repeated.  
- **Difficult to maintain**: If the discount rule changes, we must update it in multiple places.  

---

## **✅ Good Code (Follows DRY)**
### **Solution 1: Using Inheritance**
```python
class Customer:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def get_discounted_price(self, price):
        return price - (price * self.discount_rate)

class RegularCustomer(Customer):
    def __init__(self):
        super().__init__(0.05)  # 5% discount

class PremiumCustomer(Customer):
    def __init__(self):
        super().__init__(0.10)  # 10% discount

# Usage
regular = RegularCustomer()
premium = PremiumCustomer()

print(regular.get_discounted_price(100))  # ✅ 95.0
print(premium.get_discounted_price(100))  # ✅ 90.0
```
🎯 **Why?**  
- **No code duplication** → `get_discounted_price()` logic is centralized in `Customer`.  
- **Easier to extend** → If a new discount rule is added, we modify **only one place**.  

---

## **✅ Solution 2: Using Strategy Pattern (Better Extensibility)**
If we want to support **multiple discount strategies dynamically**, we can use the **Strategy Pattern**.

```python
class DiscountStrategy:
    def apply_discount(self, price):
        pass  # Abstract method

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.95  # 5% discount

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.90  # 10% discount

class Customer:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def get_discounted_price(self, price):
        return self.discount_strategy.apply_discount(price)

# Usage
regular = Customer(RegularDiscount())
premium = Customer(PremiumDiscount())

print(regular.get_discounted_price(100))  # ✅ 95.0
print(premium.get_discounted_price(100))  # ✅ 90.0
```
🎯 **Why?**  
- **No hardcoded logic** → The discount logic is **separated** into independent classes.  
- **Scalability** → New discount types can be added **without modifying existing code**.  

---

## **❌ Other Common Violations of DRY**
### **1. Repeating Queries in Database Code**
❌ **Bad (Repeated Queries)**
```python
def get_user_details(user_id):
    return execute_query(f"SELECT * FROM users WHERE id = {user_id}")

def get_user_orders(user_id):
    return execute_query(f"SELECT * FROM orders WHERE user_id = {user_id}")
```
✅ **Good (Centralized Query Handling)**
```python
class UserRepository:
    @staticmethod
    def get_user_data(user_id):
        return execute_query(f"SELECT * FROM users WHERE id = {user_id}")

    @staticmethod
    def get_user_orders(user_id):
        return execute_query(f"SELECT * FROM orders WHERE user_id = {user_id}")

# Usage
user_data = UserRepository.get_user_data(1)
user_orders = UserRepository.get_user_orders(1)
```
🎯 **Why?**  
- **Queries are managed in a single class**, making the code more **organized and reusable**.  

---

### **2. Repeating Constants in Multiple Files**
❌ **Bad (Repeated Constants)**
```python
# File 1
API_KEY = "12345"

# File 2
API_KEY = "12345"  # Duplicate
```
✅ **Good (Centralized Configuration)**
```python
# config.py
API_KEY = "12345"

# Usage
from config import API_KEY
```
🎯 **Why?**  
- **Easier maintenance** → If the API key changes, update **only one file**.  

---

### **3. Repeating HTML Templates in Web Development**
❌ **Bad (Inline HTML Repetitions)**
```html
<h1>Welcome, {{ user.name }}</h1>
<p>Your balance is {{ user.balance }}</p>

<h1>Welcome, {{ admin.name }}</h1>
<p>Your balance is {{ admin.balance }}</p>
```
✅ **Good (Reusable HTML Template)**
```html
{% macro welcome_message(user) %}
  <h1>Welcome, {{ user.name }}</h1>
  <p>Your balance is {{ user.balance }}</p>
{% endmacro %}
```
🎯 **Why?**  
- **Reduces duplication** in templates.  
- **Increases maintainability** when UI changes.  

---

| **DRY Violation** | **Solution** |
|------------------|-------------|
| **Duplicated business logic** | Use **functions, inheritance, or strategy pattern** |
| **Repeated database queries** | Centralize queries in a **repository class** |
| **Repeated constants** | Store in a **separate config file** |
| **Repeated UI elements** | Use **templating and reusable components** |





### **YAGNI (You Ain’t Gonna Need It) Principle**  
📌 **Definition:**  
**YAGNI** states that **you should not add functionality until it is absolutely necessary**.  

📌 **Core Idea:**  
- **Write only the code you need now**, not what you "think" you’ll need later.  
- Avoid **over-engineering** or **adding features that are not immediately required**.  
- **Keeps code simple, maintainable, and efficient**.  

---

## **❌ Bad Code (Violates YAGNI)**
### **Problem: Overcomplicating a Simple Task**  
Imagine we need a **basic user profile** that stores a username. But the developer decides to **add future-proofing** by implementing unnecessary features.

```python
class UserProfile:
    def __init__(self, username):
        self.username = username
        self.bio = ""  # ❌ Not needed yet
        self.profile_picture = None  # ❌ Not needed yet
        self.friends = []  # ❌ Unnecessary complexity

    def add_friend(self, friend):
        self.friends.append(friend)  # ❌ Feature not required yet

# Usage
user = UserProfile("john_doe")
print(user.username)  # ✅ Works
print(user.friends)  # ❌ Not even needed yet!
```
🎯 **Why is this bad?**  
- The **only requirement** was to store a `username`, but we added **bio, profile pictures, and friends list** unnecessarily.  
- **Bloated codebase** → Harder to maintain.  
- **Wasted development time** → Features **may never even be used**.

---

## **✅ Good Code (Follows YAGNI)**
### **Solution: Implement Only What is Needed**
```python
class UserProfile:
    def __init__(self, username):
        self.username = username  # ✅ Only the required functionality

# Usage
user = UserProfile("john_doe")
print(user.username)  # ✅ Works as expected
```
🎯 **Why is this better?**  
- **Focuses on immediate needs** → Simple, clean, and efficient.  
- If additional features like `friends` or `bio` are needed later, they **can be added incrementally**.  

---

## **❌ Another Example: Over-Engineering Functions**
### **Problem: Writing a Generic Function for a Simple Task**
❌ **Bad (Unnecessary Generalization)**
```python
def add_numbers(*args):  # ❌ Overly flexible, but not needed
    return sum(args)

print(add_numbers(5, 10))  # ✅ Works, but overkill
print(add_numbers(1, 2, 3, 4, 5, 6))  # ❌ Not needed for this case
```
✅ **Good (Keep It Simple)**
```python
def add_two_numbers(a, b):  # ✅ Does exactly what's required
    return a + b

print(add_two_numbers(5, 10))  # ✅ Works without unnecessary complexity
```
🎯 **Why?**  
- The **requirement was just to add two numbers**, so there’s **no need for a complex solution**.  
- **Simpler functions = Easier debugging and testing**.  

---

## **❌ Over-Engineering with Design Patterns**
### **Problem: Using a Factory Pattern for a Simple Class**
Imagine a **simple `Logger` class** that prints messages.  

❌ **Bad (Over-Engineering with Factory)**
```python
class Logger:
    def log(self, message):
        print(f"Log: {message}")

class LoggerFactory:
    @staticmethod
    def get_logger():
        return Logger()

logger = LoggerFactory.get_logger()  # ❌ Unnecessary factory
logger.log("System started")  # ✅ Works, but overkill
```
✅ **Good (Direct Instantiation)**
```python
class Logger:
    def log(self, message):
        print(f"Log: {message}")

logger = Logger()  # ✅ Direct and simple
logger.log("System started")
```
🎯 **Why?**  
- The **Factory Pattern is unnecessary** for a simple `Logger` class.  
- **Over-engineering adds complexity without benefit**.  
- If a Factory is needed **later**, it can be added **when required**.

---

## **🔹 When Should You Apply YAGNI?**
| **Scenario** | **Apply YAGNI?** | **Reason** |
|-------------|------------|---------|
| Writing extra methods “just in case” | ✅ Yes | Unused code increases complexity |
| Creating a database table for features not yet planned | ✅ Yes | Wasted storage, maintenance cost |
| Using a complex design pattern when a simple function works | ✅ Yes | Over-engineering |
| Adding a new feature based on actual user feedback | ❌ No | Needed functionality |
| Writing unit tests for critical code | ❌ No | Testing is necessary |

---

## **🔹 How to Answer in an Interview?**
**1. Define YAGNI clearly:**  
> "YAGNI stands for 'You Ain’t Gonna Need It,' meaning we should not add features unless they are required."

**2. Explain why avoiding premature optimization is important:**  
> "Adding unnecessary code increases complexity, maintenance cost, and bugs."

**3. Provide an example of over-engineering and refactor it using YAGNI.**  
> Example: Overuse of a Factory Pattern when simple class instantiation is enough.

**4. Conclude with the benefits:**  
> "Following YAGNI makes codebase **simpler, more maintainable, and faster to develop**."

---

✅ **Only write code for what is needed today, not for a hypothetical future.**  
✅ **Avoid premature optimizations or complex patterns when simpler solutions exist.**  
✅ **Refactor only when new requirements emerge.**  
✅ **Keeps the codebase clean, readable, and maintainable.**  


### **KISS (Keep It Simple, Stupid) Principle**  

📌 **Definition:**  
The **KISS principle** states that **systems should be as simple as possible**. Avoid **unnecessary complexity** and aim for **clear, maintainable, and efficient** code.  

📌 **Core Idea:**  
- **Simple code is easier to read, debug, and extend.**  
- **Avoid over-engineering** when a straightforward solution works.  
- **Make decisions based on actual needs, not assumptions.**  

---

## **1️⃣ ❌ Bad Code (Violates KISS)**
### **Problem: Overcomplicated If-Else Conditions**
❌ **Bad Code (Complex Conditional Logic)**
```python
def get_discount(price, user_type):
    if user_type == "premium":
        if price > 500:
            return price * 0.80  # 20% discount
        else:
            return price * 0.90  # 10% discount
    elif user_type == "regular":
        if price > 500:
            return price * 0.90  # 10% discount
        else:
            return price * 0.95  # 5% discount
    else:
        return price  # No discount
```
### **🛑 What's wrong?**
- Nested conditions make it **hard to read** and **difficult to maintain**.
- Adding a new discount rule **requires modifying multiple parts of the function**.

✅ **Good Code (Follows KISS)**
```python
def get_discount(price, discount_rate):
    return price * (1 - discount_rate)

discount_rates = {"premium": 0.10, "regular": 0.05}
user_type = "premium"

discounted_price = get_discount(600, discount_rates.get(user_type, 0))
print(discounted_price)  # ✅ 540.0
```
🎯 **Why is this better?**  
- **Removes unnecessary nesting** and simplifies the logic.  
- **Easy to update** → Adding a new discount just requires modifying `discount_rates`.  

---

## **2️⃣ ❌ Overcomplicated Loops (Violates KISS)**
### **Problem: Using a Complex Loop for a Simple Task**
❌ **Bad Code (Unnecessarily Complex)**
```python
numbers = [1, 2, 3, 4, 5]
sum_numbers = 0

for i in range(len(numbers)):  # ❌ Overly complicated loop
    sum_numbers += numbers[i]

print(sum_numbers)
```
✅ **Good Code (Follows KISS)**
```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # ✅ Simple and efficient
```
🎯 **Why?**  
- Uses Python’s **built-in `sum()` function**, making the code **shorter and clearer**.  
- **Improves readability and performance**.  

---

## **3️⃣ ❌ Over-Engineering with Design Patterns (Violates KISS)**
### **Problem: Using Factory Pattern for a Simple Task**
❌ **Bad Code (Overuse of Factory Pattern)**
```python
class Logger:
    def log(self, message):
        print(f"Log: {message}")

class LoggerFactory:
    @staticmethod
    def get_logger():
        return Logger()

logger = LoggerFactory.get_logger()  # ❌ Unnecessary Factory
logger.log("System started")
```
✅ **Good Code (Follows KISS)**
```python
class Logger:
    def log(self, message):
        print(f"Log: {message}")

logger = Logger()  # ✅ Direct instantiation is simpler
logger.log("System started")
```
🎯 **Why?**  
- **Removes unnecessary complexity** (No need for `LoggerFactory`).  
- **Only use design patterns when necessary**—Factory **only makes sense if multiple Logger types exist**.  

---

## **4️⃣ ❌ Overcomplicated Functionality (Violates KISS)**
### **Problem: Adding Features That Aren’t Needed**
❌ **Bad Code (Unnecessary Future-Proofing)**
```python
class Calculator:
    def __init__(self):
        self.history = []  # ❌ Extra feature not needed

    def add(self, a, b):
        result = a + b
        self.history.append(result)  # ❌ Not required for simple addition
        return result
```
✅ **Good Code (Follows KISS)**
```python
def add(a, b):
    return a + b  # ✅ Simple and effective
```
🎯 **Why?**  
- **Focuses on the immediate requirement** (Addition function).  
- **Avoids unnecessary features** (history tracking can be added **only if needed**).  

---

## **🔹 When Should You Apply KISS?**
| **Scenario** | **Apply KISS?** | **Reason** |
|-------------|------------|---------|
| Writing simple functions | ✅ Yes | Avoid unnecessary complexity |
| Using built-in functions instead of manual loops | ✅ Yes | Improves readability & performance |
| Adding features based on assumptions | ❌ No | Leads to feature bloat |
| Using complex design patterns for small tasks | ❌ No | Over-engineering |

---

## **🔹 How to Answer in an Interview?**
**1. Define KISS clearly:**  
> "The KISS principle stands for **Keep It Simple, Stupid**—code should be **as simple as possible** while fulfilling its purpose."

**2. Explain why simplicity is important:**  
> "Simple code is easier to **read, test, debug, and maintain**, reducing development time and technical debt."

**3. Provide an example of overly complex code and how to simplify it.**  
> Example: **Replacing deep nested if-else conditions with a dictionary lookup.**

**4. Conclude with benefits:**  
> "Following KISS ensures **faster development, better maintainability, and fewer bugs.**"

---

## **💡 Key Takeaways**
✅ **Write simple, clear, and maintainable code.**  
✅ **Avoid over-engineering and unnecessary features.**  
✅ **Use built-in functions and straightforward solutions whenever possible.**  
✅ **Design for current needs, not hypothetical future scenarios.**  


# [Coursera - Object-Oriented Design](https://www.coursera.org/learn/object-oriented-design)


## Design Patterns
### Creational Patterns
Singleton
Factory Method
Builder
Abstract Factory
Prototype


### Structural Patterns	
Adapter  
Bridge
Composite
Decorator
Facade
Flyweight
Proxy


### Behavioral Patterns
Chain of Responsibility
Command
Iterator
Mediator
Memento
Observer
State
Strategy
Template Method
Visitor


🗂️ UML


Class Diagram
Use Case Diagram
Sequence Diagram
Activity Diagram
State Machine Diagram




💻 Low Level Design Interview Problems


### Easy


Design Parking Lot
Design a Vending Machine
Design Stack Overflow
Design Logging Framework
Design Coffee Vending Machine
Design Traffic Signal Control System
Design a Task Management System


### Medium


Design Pub Sub System
Design Tic Tac Toe Game
Design Car Rental System
Design an ATM
Design Hotel Management System
Design LinkedIn
Design a Social Network like Facebook
Design an Elevator System
Design a Library Management System
Design Restaurant Management System
Design Airline Management System
Design a Digital Wallet System
Design an Online Auction System
Design a Concert Ticket Booking System
Design a Cache using LRU Eviction Policy



### Hard


Design Movie Ticket Booking System
Design Splitwise
Design a Snake and Ladder game
Design Online Shopping System like Amazon
Design Online Stock Brokerage System
Design CricInfo
Design Chess Game
Design Ride-Sharing Service (like Uber)
Design Online Food Delivery Service (like Swiggy)
Design Music Streaming Service (like Spotify)
Design University Course Registration System


📚 Books
Head First Design Patterns
Clean Code
Refactoring: Improving the Design of Existing Code