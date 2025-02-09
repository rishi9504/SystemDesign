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
### **Creational Design Patterns (LLD Interview Explanation)**  

📌 **Definition:**  
Creational design patterns are used to **control object creation**, ensuring flexibility, scalability, and reusability.  

📌 **Why are Creational Patterns Important?**  
- **Encapsulate object creation logic** → Avoids tight coupling.  
- **Improve performance** → Avoids unnecessary object creation.  
- **Enable different object instantiation methods** (lazy loading, pooling, cloning).  

---

## **Types of Creational Design Patterns**
| **Pattern** | **Purpose** | **Example Use Case** |
|------------|------------|-----------------|
| **Singleton** | Ensures only **one instance** of a class exists. | Database connection, Logger |
| **Factory Method** | Delegates object creation to a **subclass or method**. | Payment Gateway (CreditCard, UPI, PayPal) |
| **Abstract Factory** | Creates **families of related objects** without specifying their concrete classes. | UI Components (MacOS vs. Windows UI) |
| **Builder** | Constructs **complex objects step-by-step**. | Creating complex objects like a Burger (Bun, Patty, Sauce) |
| **Prototype** | Creates **clones** of an existing object. | Game Character Cloning, Object Caching |

---

## **1️⃣ Singleton Pattern → Ensures One Instance**
### **Problem:**  
We need a **single shared object** (e.g., a **Logger** or **Database Connection**) instead of creating multiple instances.  

### **❌ Bad Code (Without Singleton)**
```python
class Logger:
    def log(self, message):
        print(f"Log: {message}")

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # ❌ False (Two separate instances)
```
💡 **Fix: Singleton Pattern** → Ensures only **one instance exists**.  

### **✅ Good Code (Singleton)**
```python
class Logger:
    _instance = None  # Private class attribute

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # ✅ True (Same instance)
```
🎯 **Why?**  
- Prevents **multiple instances** from being created.  
- Saves **memory** and **ensures centralized logging**.  

---

## **2️⃣ Factory Method → Encapsulates Object Creation**
### **Problem:**  
We need to create different **types of payments** (Credit Card, UPI, PayPal). Instead of using **if-else conditions**, use **Factory Method**.  

### **❌ Bad Code (Without Factory)**
```python
class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processing Credit Card payment of ${amount}"

class UpiPayment:
    def process_payment(self, amount):
        return f"Processing UPI payment of ${amount}"

payment_type = "credit_card"
if payment_type == "credit_card":
    payment = CreditCardPayment()
elif payment_type == "upi":
    payment = UpiPayment()
```
💡 **Fix: Factory Method** → Let a **factory class** create objects.  

### **✅ Good Code (Factory Pattern)**
```python
class Payment:
    def process_payment(self, amount):
        pass  # Abstract method

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing Credit Card payment of ${amount}"

class UpiPayment(Payment):
    def process_payment(self, amount):
        return f"Processing UPI payment of ${amount}"

class PaymentFactory:
    @staticmethod
    def get_payment_method(method):
        if method == "credit_card":
            return CreditCardPayment()
        elif method == "upi":
            return UpiPayment()
        else:
            raise ValueError("Invalid payment method")

# Usage
payment = PaymentFactory.get_payment_method("credit_card")
print(payment.process_payment(100))  # ✅ Processing Credit Card payment of $100
```
🎯 **Why?**  
- **Centralized object creation** → No `if-else` logic scattered in the code.  
- **Easier to extend** → Adding a new payment method doesn’t require modifying existing code.  

---

## **3️⃣ Abstract Factory → Creates Families of Objects**
### **Problem:**  
We need **different UI elements** for **MacOS and Windows**, but their implementations vary.  

💡 **Fix: Abstract Factory** → Provides a **common interface** to create different object families.  

### **✅ Good Code (Abstract Factory Pattern)**
```python
class Button:
    def render(self):
        pass  # Abstract method

class MacButton(Button):
    def render(self):
        return "Rendering MacOS Button"

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"

class UIFactory:
    @staticmethod
    def create_button(os_type):
        if os_type == "mac":
            return MacButton()
        elif os_type == "windows":
            return WindowsButton()
        else:
            raise ValueError("Unsupported OS")

# Usage
button = UIFactory.create_button("mac")
print(button.render())  # ✅ Rendering MacOS Button
```
🎯 **Why?**  
- **Creates families of related objects** without hardcoding dependencies.  
- **Easily switch between different UI implementations.**  

---

## **4️⃣ Builder Pattern → Step-by-Step Object Creation**
### **Problem:**  
We need to create a **Burger** with multiple components (bun, patty, sauce). Instead of using a **long constructor**, use a **Builder Pattern**.  

### **✅ Good Code (Builder Pattern)**
```python
class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.sauce = None

    def __str__(self):
        return f"Burger with {self.bun}, {self.patty}, and {self.sauce}"

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self, bun):
        self.burger.bun = bun
        return self

    def add_patty(self, patty):
        self.burger.patty = patty
        return self

    def add_sauce(self, sauce):
        self.burger.sauce = sauce
        return self

    def build(self):
        return self.burger

# Usage
burger = BurgerBuilder().add_bun("Sesame").add_patty("Beef").add_sauce("BBQ").build()
print(burger)  # ✅ Burger with Sesame, Beef, and BBQ
```
🎯 **Why?**  
- **Step-by-step construction** of a complex object.  
- **Avoids long constructor arguments.**  

---

## **5️⃣ Prototype Pattern → Cloning Objects**
### **Problem:**  
Creating a new object from scratch **is expensive**. Instead, **clone** an existing object.  

### **✅ Good Code (Prototype Pattern)**
```python
import copy

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def clone(self):
        return copy.deepcopy(self)

# Usage
car1 = Car("Tesla", "Model S")
car2 = car1.clone()

print(car2.brand, car2.model)  # ✅ Tesla Model S (Cloned)
```
🎯 **Why?**  
- **Faster object creation** → No need to reinitialize.  
- Useful in **game development, object pooling, and AI training models**.  

---

## **🔹 Summary of Creational Patterns**
| **Pattern** | **Purpose** | **Example Use Case** |
|------------|------------|-----------------|
| **Singleton** | Ensures **one instance** of a class exists. | Database connection, Logger |
| **Factory Method** | Delegates object creation to a **subclass or method**. | Payment Gateway (CreditCard, UPI, PayPal) |
| **Abstract Factory** | Creates **families of related objects**. | UI Components (MacOS vs. Windows UI) |
| **Builder** | Constructs **complex objects step-by-step**. | Burger Creation, Car Configuration |
| **Prototype** | Clones objects instead of creating new ones. | Game Character Cloning, Object Caching |

### **Real-World System Design Applications of Creational Design Patterns**  

In **Low-Level Design (LLD) and System Design interviews**, demonstrating how **creational patterns** apply to **real-world systems** helps show your **design thinking and scalability considerations**.  

---

## **1️⃣ Singleton Pattern → Database Connection Pool (Scaling Web Applications)**
📌 **Use Case:** **Databases** like MySQL, PostgreSQL, and MongoDB **should have a single connection pool** to prevent **resource exhaustion**.

💡 **Why Singleton?**  
- Ensures **only one instance** of the **database connection pool** exists.  
- Prevents **creating multiple connections** that could overwhelm the system.  

✅ **Real-World Implementation (Database Connection Pool)**
```python
import sqlite3

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect("database.db")  # ✅ Single DB connection
        return cls._instance

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # ✅ True (Same instance)
```
🎯 **Where is this used?**  
- **Django ORM, SQLAlchemy** → Use connection pooling to **avoid repeated connections**.  
- **Cloud Services (AWS RDS, Google Cloud SQL)** → Maintain **a single connection manager** for clients.  

---

## **2️⃣ Factory Method → Payment Gateway Integration (E-commerce, Subscription Services)**
📌 **Use Case:** Applications like **Amazon, Netflix, Stripe, and PayPal** support **multiple payment methods (Credit Card, UPI, PayPal, Apple Pay)**.  

💡 **Why Factory Method?**  
- Avoids **hardcoding payment methods** in a single class.  
- Makes it **easy to add new payment methods without modifying existing code**.  

✅ **Real-World Implementation (Payment Gateway)**
```python
class Payment:
    def process_payment(self, amount):
        pass  # Abstract method

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing Credit Card payment of ${amount}"

class UpiPayment(Payment):
    def process_payment(self, amount):
        return f"Processing UPI payment of ${amount}"

class PaymentFactory:
    @staticmethod
    def get_payment_method(method):
        if method == "credit_card":
            return CreditCardPayment()
        elif method == "upi":
            return UpiPayment()
        else:
            raise ValueError("Invalid payment method")

# Usage
payment = PaymentFactory.get_payment_method("credit_card")
print(payment.process_payment(100))  # ✅ Processing Credit Card payment of $100
```
🎯 **Where is this used?**  
- **Stripe, PayPal, Razorpay** → Dynamically select the correct payment processor.  
- **E-commerce Platforms (Amazon, Shopify, Flipkart)** → Support multiple payment methods **without modifying core business logic**.  

---

## **3️⃣ Abstract Factory → UI Frameworks (Cross-Platform Development)**
📌 **Use Case:** **Cross-platform UI frameworks** (Flutter, React Native, Electron) need to **generate different UI elements for different operating systems**.  

💡 **Why Abstract Factory?**  
- Allows **creating UI components** that are **platform-specific** without modifying the main application.  

✅ **Real-World Implementation (Cross-Platform UI)**
```python
class Button:
    def render(self):
        pass  # Abstract method

class MacButton(Button):
    def render(self):
        return "Rendering MacOS Button"

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"

class UIFactory:
    @staticmethod
    def create_button(os_type):
        if os_type == "mac":
            return MacButton()
        elif os_type == "windows":
            return WindowsButton()
        else:
            raise ValueError("Unsupported OS")

# Usage
button = UIFactory.create_button("mac")
print(button.render())  # ✅ Rendering MacOS Button
```
🎯 **Where is this used?**  
- **Flutter, React Native, Electron** → Render **different UI components** for iOS, Android, and Windows.  
- **Video Editing Software (Adobe Premiere, Final Cut Pro)** → Uses **different UI themes** based on the OS.  

---

## **4️⃣ Builder Pattern → Complex Object Creation (Fast Food Ordering, Game Characters)**
📌 **Use Case:** **Creating complex objects** like **Burgers (McDonald's), Cars (Tesla), or Game Characters (PUBG, Fortnite)**.  

💡 **Why Builder?**  
- Avoids **long constructors** that make object creation **messy**.  
- Enables **step-by-step customization** without changing the base class.  

✅ **Real-World Implementation (Burger Builder for Fast Food App)**
```python
class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.sauce = None

    def __str__(self):
        return f"Burger with {self.bun}, {self.patty}, and {self.sauce}"

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self, bun):
        self.burger.bun = bun
        return self

    def add_patty(self, patty):
        self.burger.patty = patty
        return self

    def add_sauce(self, sauce):
        self.burger.sauce = sauce
        return self

    def build(self):
        return self.burger

# Usage
burger = BurgerBuilder().add_bun("Sesame").add_patty("Beef").add_sauce("BBQ").build()
print(burger)  # ✅ Burger with Sesame, Beef, and BBQ
```
🎯 **Where is this used?**  
- **McDonald's, Domino’s, Subway** → Custom order system (choose bun, toppings, sauce).  
- **Tesla Car Configurator** → Users select **battery, color, autopilot features step-by-step**.  
- **Game Character Customization (PUBG, Fortnite)** → Players choose **armor, weapons, skills, outfits**.  

---

## **5️⃣ Prototype Pattern → Object Caching & Cloning (Game Development, AI Models)**
📌 **Use Case:**  
Creating a new object **from scratch is expensive** (e.g., **Game characters, AI models**). Instead, **clone an existing object**.

💡 **Why Prototype?**  
- Reduces **memory usage and processing time**.  
- Avoids **re-initializing complex objects from scratch**.  

✅ **Real-World Implementation (Game Character Cloning)**
```python
import copy

class GameCharacter:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    def clone(self):
        return copy.deepcopy(self)

# Usage
character1 = GameCharacter("Knight", 100, 50)
character2 = character1.clone()

print(character2.name, character2.health, character2.armor)  # ✅ Knight 100 50
```
🎯 **Where is this used?**  
- **Game Engines (Unity, Unreal Engine)** → Clone NPCs and enemies **without recalculating attributes**.  
- **AI Model Training (TensorFlow, PyTorch)** → Clone deep learning models for **distributed training**.  

---

## **🔹 Summary: Creational Patterns in Real-World Systems**
| **Pattern** | **Real-World Application** |
|------------|---------------------|
| **Singleton** | Database Connection Pool (AWS RDS, MySQL) |
| **Factory Method** | Payment Gateway (Stripe, PayPal, UPI) |
| **Abstract Factory** | UI Frameworks (Flutter, Electron, React Native) |
| **Builder** | Custom Orders (Tesla Cars, McDonald’s Burgers) |
| **Prototype** | Game Character Cloning (Fortnite, PUBG), AI Model Replication |

---

### **How to Answer in an LLD Interview?**
1️⃣ Define the **pattern** and explain **why it is needed**.  
2️⃣ Provide a **real-world use case** (e.g., payment gateways for Factory Method).  
3️⃣ Explain **how it improves scalability & maintainability**.  
4️⃣ Show **Python code implementation**.  

### **Scalability Considerations for Creational Design Patterns in Large-Scale Systems**

When designing systems that handle large-scale traffic, data, and user loads, **creational patterns** help ensure that the system is **efficient, maintainable, and scalable**. Here’s how each creational pattern can be scaled for real-world applications:

---

## **1️⃣ Singleton Pattern → Database Connection Pool in Scalable Systems**
**Scenario:** A large-scale system needs to manage **multiple database connections** but with limited resources. Multiple instances of the **Singleton** pattern can help avoid excessive memory usage and ensure **efficiency** in a multi-threaded environment.

### **Challenges in Large-Scale Systems:**
- **Concurrent Connections:** The application might handle thousands of simultaneous requests.
- **Resource Management:** Opening new connections to the database on every request can cause **resource exhaustion**.

### **How Singleton Helps:**
- **Single Instance of Connection Pool:** Only one connection pool object exists, ensuring efficient resource usage. 
- **Thread Safety:** Implement thread-safe access to the connection pool, ensuring **each thread** retrieves the connection in a non-blocking manner.
- **Lazy Initialization:** Connections are initialized only when needed (on-demand), reducing resource usage at startup.

### **Example with Connection Pool**
```python
import threading
import sqlite3

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DatabaseConnection, cls).__new__(cls)
                cls._instance.connection = sqlite3.connect("large_scale_db.db")  # Connection Pool
        return cls._instance

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # ✅ True (Same instance)
```
🎯 **Scalability Benefit:**  
- **Resource-efficient**: No need to open new connections frequently.
- **Handles load spikes** with **single-threaded connection pooling**.

---

## **2️⃣ Factory Method → Scalable Payment Gateway in E-commerce Platforms**
**Scenario:** An e-commerce platform (e.g., **Amazon, Shopify**) needs to handle **multiple payment methods** (Credit Card, UPI, PayPal, etc.), each with different integration requirements.

### **Challenges in Large-Scale Systems:**
- **Multiple Payment Processors:** New payment processors can be integrated over time.
- **Separation of Concerns:** Business logic should not be dependent on specific payment processing classes.

### **How Factory Method Helps:**
- **Dynamic Object Creation:** The factory creates objects based on configuration, making it **easy to add new payment methods** without modifying core logic.
- **Decouples Business Logic:** Clients don’t need to know the specific payment method being used, reducing tight coupling and making the system **more maintainable**.

### **Scalable Example for Payment Methods**
```python
class Payment:
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing Credit Card payment of ${amount}"

class UpiPayment(Payment):
    def process_payment(self, amount):
        return f"Processing UPI payment of ${amount}"

class PaymentFactory:
    @staticmethod
    def get_payment_method(method):
        if method == "credit_card":
            return CreditCardPayment()
        elif method == "upi":
            return UpiPayment()
        else:
            raise ValueError("Unsupported payment method")

# Usage
payment_method = PaymentFactory.get_payment_method("credit_card")
print(payment_method.process_payment(100))  # ✅ Processing Credit Card payment of $100
```
🎯 **Scalability Benefit:**  
- **Dynamic payment method selection** based on user preferences.
- **New payment methods can be integrated** by simply adding new classes and updating the factory.

---

## **3️⃣ Abstract Factory → Cross-Platform UI in Mobile Apps**
**Scenario:** A mobile application needs to display a consistent **UI across platforms** (iOS, Android) while maintaining platform-specific components (e.g., buttons, text inputs).

### **Challenges in Large-Scale Systems:**
- **Multiple Platforms:** Codebase should remain **consistent** across platforms but allow platform-specific variations.
- **Maintainability:** Adding new UI components should not require changes in all platform code.

### **How Abstract Factory Helps:**
- **Platform-Specific UI Creation:** The abstract factory creates UI elements based on the platform, ensuring **consistent UI behavior** across devices.
- **Easily Extendable:** As new platforms or UI components are added (e.g., Dark Mode), they can be **added without modifying existing code**.

### **Example for Cross-Platform UI Creation**
```python
class Button:
    def render(self):
        pass  # Abstract method

class MacButton(Button):
    def render(self):
        return "Rendering MacOS Button"

class AndroidButton(Button):
    def render(self):
        return "Rendering Android Button"

class UIFactory:
    @staticmethod
    def create_button(os_type):
        if os_type == "mac":
            return MacButton()
        elif os_type == "android":
            return AndroidButton()
        else:
            raise ValueError("Unsupported OS")

# Usage
button = UIFactory.create_button("mac")
print(button.render())  # ✅ Rendering MacOS Button
```
🎯 **Scalability Benefit:**  
- **Single codebase** for both iOS and Android.
- New platforms or UI components can be added without altering existing ones.

---

## **4️⃣ Builder Pattern → Scalable Product Customization in E-Commerce**
**Scenario:** **Car manufacturers (Tesla)** or **customizable product websites** (e.g., **Dell laptops**) allow customers to customize products with different **configurations** (e.g., color, features, specs).

### **Challenges in Large-Scale Systems:**
- **Complex Customizations:** Creating customized products requires combining various components in a specific order.
- **Maintainability:** Maintaining multiple constructors with varying parameters becomes **complex**.

### **How Builder Helps:**
- **Separation of Object Construction:** The builder pattern allows creating complex objects **step-by-step**.
- **Flexibility:** The builder can handle different configurations and ensure that all components are correctly assembled.

### **Example for Car Configuration (Tesla)**
```python
class Car:
    def __init__(self):
        self.color = None
        self.engine_type = None
        self.safety_features = []

    def __str__(self):
        return f"Car with {self.color} color, {self.engine_type} engine, features: {', '.join(self.safety_features)}"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_color(self, color):
        self.car.color = color
        return self

    def add_engine(self, engine_type):
        self.car.engine_type = engine_type
        return self

    def add_safety_features(self, *features):
        self.car.safety_features.extend(features)
        return self

    def build(self):
        return self.car

# Usage
car = CarBuilder().add_color("Red").add_engine("Electric").add_safety_features("Airbags", "ABS").build()
print(car)  # ✅ Car with Red color, Electric engine, features: Airbags, ABS
```
🎯 **Scalability Benefit:**  
- **Flexible configurations** without complex constructors.
- New **features and configurations** can be added without modifying core class logic.

---

## **5️⃣ Prototype Pattern → Cloning Large-Scale Game Worlds or AI Models**
**Scenario:** In **gaming**, environments (e.g., **game worlds, characters, levels**) may need to be **cloned** rapidly to create **multiple instances** (NPCs, enemies).

### **Challenges in Large-Scale Systems:**
- **Complex Object Creation:** Creating a game world from scratch for each new character or enemy is **resource-heavy**.
- **Performance:** **Cloning** existing objects is more **efficient** than creating from scratch.

### **How Prototype Helps:**
- **Clone Objects Efficiently:** Use cloning to create **multiple copies** of objects (e.g., NPCs, enemies) instead of creating new ones from scratch.
- **Memory Efficiency:** Clone **base game objects** instead of reinitializing them every time.

### **Example for Cloning Game Characters**
```python
import copy

class GameCharacter:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def clone(self):
        return copy.deepcopy(self)

# Usage
main_character = GameCharacter("Hero", 100, 50)
enemy_character = main_character.clone()  # Clone for enemy

print(enemy_character.name, enemy_character.health)  # ✅ Hero 100
```
🎯 **Scalability Benefit:**  
- **Efficient cloning** reduces the need to reinitialize characters and environments.
- **Faster object creation** when the game world becomes large.

---

## **Conclusion: Creational Patterns and Scalability**
| **Pattern** | **Scalability Consideration** | **Example** |
|-------------|------------------------------|-------------|
| **Singleton** | Ensures **single instance** of shared resources like DB connection pools. | Database connection pools (AWS RDS, MySQL) |
| **Factory Method** | Handles the **addition of new object types** without modifying core logic. | Payment gateway integration (Stripe, PayPal) |
| **Abstract Factory** | **Generates platform-specific objects** while maintaining a consistent interface. | Cross-platform UI (Flutter, React Native) |
| **Builder** | **Constructs complex objects step-by-step**, allowing customization. | Custom orders (Tesla Cars, McDonald’s Burgers) |
| **Prototype** | **Clones objects** to improve performance and memory efficiency. | Game object cloning (Fortnite, PUBG), AI model replication |

---

By applying these patterns in large-scale systems, you can **enhance performance, scalability**, and **maintainability**, ensuring the system can grow with the business needs.




### **Structural Design Patterns (LLD Interview Explanation)**

📌 **Definition:**  
Structural design patterns focus on **how classes and objects are composed** to form **larger structures** while ensuring that the system remains flexible and maintainable. These patterns simplify the **design of complex structures** by **reducing dependencies** and promoting **efficient relationships** between components.

📌 **Why are Structural Patterns Important?**  
- **Simplify relationships** between classes and objects.  
- Help with **flexible system design** while **reducing coupling**.  
- Allow components to be **interchangeable** and **scalable**.

---

## **Common Structural Patterns:**
1. **Adapter**
2. **Bridge**
3. **Composite**
4. **Decorator**
5. **Facade**
6. **Flyweight**
7. **Proxy**

---

### **1️⃣ Adapter Pattern → Compatibility Between Different Interfaces**
📌 **Use Case:**  
When two incompatible interfaces need to **work together**, the **Adapter Pattern** converts one interface into another.

💡 **Why Adapter?**  
- To make an **existing system work with another system** without modifying the system itself.  
- To **adapt** the interface of a class to meet the needs of another.

✅ **Example:**  
A `Target` class expects a method named `request()`, but the `Adaptee` class has a method named `specificRequest()`. The Adapter will bridge the gap.

```python
class Adaptee:
    def specific_request(self):
        return "Specific Request"

class Target:
    def request(self):
        pass  # The method expected by the client

class Adapter(Target, Adaptee):
    def request(self):
        return self.specific_request()  # Adapts the specific_request() to request()

# Usage
adapter = Adapter()
print(adapter.request())  # ✅ Specific Request
```
🎯 **Where is this used?**  
- **Third-party libraries** integration.  
- **Legacy systems** integration with newer frameworks.

---

### **2️⃣ Bridge Pattern → Decouple Abstraction from Implementation**
📌 **Use Case:**  
When both the **abstraction** (the interface) and the **implementation** (the actual work) may vary independently, the **Bridge Pattern** decouples them.

💡 **Why Bridge?**  
- To allow changes in the **abstraction** and **implementation** independently without affecting each other.  
- Commonly used when you have **two orthogonal dimensions** (e.g., a **shape** and **color**).

✅ **Example:**
Imagine you have a `Shape` class and a `Color` class, and you want to combine them. Instead of inheriting both, use the **Bridge Pattern** to keep them separate but connected.

```python
class Color:
    def fill(self):
        pass  # Abstract method

class Red(Color):
    def fill(self):
        return "Red Color"

class Blue(Color):
    def fill(self):
        return "Blue Color"

class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass  # Abstract method

class Circle(Shape):
    def draw(self):
        return f"Drawing Circle with {self.color.fill()}"

class Square(Shape):
    def draw(self):
        return f"Drawing Square with {self.color.fill()}"

# Usage
circle = Circle(Red())
print(circle.draw())  # ✅ Drawing Circle with Red Color

square = Square(Blue())
print(square.draw())  # ✅ Drawing Square with Blue Color
```
🎯 **Where is this used?**  
- **Graphics frameworks** (different shapes with different colors).  
- **UI frameworks** with multiple themes and controls.

---

### **3️⃣ Composite Pattern → Treat Individual Objects and Compositions Uniformly**
📌 **Use Case:**  
The **Composite Pattern** is used when you need to **treat individual objects** and **compositions of objects** in a uniform manner. It allows you to **build tree-like structures** where leaves and branches are treated uniformly.

💡 **Why Composite?**  
- **Simplifies the client code** by treating single objects and composite objects (groups of objects) the same way.  
- Often used in **hierarchical structures** like file systems or organizational charts.

✅ **Example:**  
Imagine you have a `Graphic` interface, with concrete objects like `Circle` and `Rectangle`. Both can be treated the same way in a composite structure.

```python
class Graphic:
    def draw(self):
        pass  # Abstract method

class Circle(Graphic):
    def draw(self):
        return "Drawing Circle"

class Rectangle(Graphic):
    def draw(self):
        return "Drawing Rectangle"

class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def draw(self):
        return ", ".join([graphic.draw() for graphic in self.graphics])

# Usage
circle = Circle()
rectangle = Rectangle()
composite = CompositeGraphic()
composite.add(circle)
composite.add(rectangle)

print(composite.draw())  # ✅ Drawing Circle, Drawing Rectangle
```
🎯 **Where is this used?**  
- **File systems** (files and directories are treated as a single entity).  
- **UI component trees** (buttons, panels, and forms).  

---

### **4️⃣ Decorator Pattern → Add Responsibilities to Objects Dynamically**
📌 **Use Case:**  
The **Decorator Pattern** allows you to **add behavior** to an object **dynamically**. It enhances functionality without modifying the object itself.

💡 **Why Decorator?**  
- To add functionality to an object without changing its code or subclassing.  
- To provide **extensible and reusable functionality**.

✅ **Example:**  
Imagine a `Car` class, and you want to **dynamically add features** (like air conditioning, sunroof) to the car.

```python
class Car:
    def assemble(self):
        return "Basic Car"

class CarDecorator:
    def __init__(self, car: Car):
        self._car = car

    def assemble(self):
        return self._car.assemble()

class AirConditioningDecorator(CarDecorator):
    def assemble(self):
        return f"{self._car.assemble()} with Air Conditioning"

class SunroofDecorator(CarDecorator):
    def assemble(self):
        return f"{self._car.assemble()} with Sunroof"

# Usage
basic_car = Car()
print(basic_car.assemble())  # ✅ Basic Car

ac_car = AirConditioningDecorator(basic_car)
print(ac_car.assemble())  # ✅ Basic Car with Air Conditioning

sunroof_car = SunroofDecorator(ac_car)
print(sunroof_car.assemble())  # ✅ Basic Car with Air Conditioning with Sunroof
```
🎯 **Where is this used?**  
- **GUI toolkits** (adding buttons, text boxes, and other widgets dynamically).  
- **Logging frameworks** (dynamic log formatting and levels).  

---

### **5️⃣ Facade Pattern → Simplify Complex Subsystems**
📌 **Use Case:**  
The **Facade Pattern** provides a **simplified interface** to a complex system. It is used when a system has a lot of **complex interactions**, and you want to **hide that complexity** behind a simpler interface.

💡 **Why Facade?**  
- **Simplifies the interface** for clients.  
- **Reduces the number of interactions** a client has to make with a system.

✅ **Example:**  
Imagine a system for **video conversion**, which involves many complex processes like loading video, compressing it, and saving it.

```python
class VideoConverter:
    def load_video(self):
        return "Video loaded"

    def compress_video(self):
        return "Video compressed"

    def save_video(self):
        return "Video saved"

class VideoConversionFacade:
    def __init__(self):
        self.converter = VideoConverter()

    def convert_video(self):
        print(self.converter.load_video())
        print(self.converter.compress_video())
        print(self.converter.save_video())

# Usage
facade = VideoConversionFacade()
facade.convert_video()  # ✅ Simplified client interaction
```
🎯 **Where is this used?**  
- **Library systems** (providing a simple API for complex library functions).  
- **Video editing software** (simplified actions for complex processing).

---

### **6️⃣ Flyweight Pattern → Reuse Shared Objects for Memory Efficiency**
📌 **Use Case:**  
The **Flyweight Pattern** is used when an application needs to handle **large numbers of objects** with **identical data**. Instead of storing duplicate data, the flyweight pattern ensures **shared data** is reused.

💡 **Why Flyweight?**  
- **Reduces memory usage** by sharing common data.  
- **Improves performance** by reducing the number of objects created.

✅ **Example:**  
Imagine you're creating a **text editor** where many characters (letters) may appear multiple times.

```python
class Character:
    def __init__(self, character):
        self.character = character

class CharacterFactory:
    _characters = {}

    @staticmethod
    def get_character(character):
        if character not in CharacterFactory._characters:
            CharacterFactory._characters[character] = Character(character)
        return CharacterFactory._characters[character]

# Usage
a = CharacterFactory.get_character('A')
b = CharacterFactory.get_character('B')
c = CharacterFactory.get_character('A')

print(a is c)  # ✅ True (Shared object)
```
🎯 **Where is this used?**  
- **Text editors** (reusing common characters).  
- **Web page rendering** (shared resources like images or fonts).

---

### **7️⃣ Proxy Pattern → Control Access to Objects**
📌 **Use Case:**  
The **Proxy Pattern** provides an **object** that acts as a placeholder for another object. It is used when access to the real object should be **controlled** (e.g., lazy initialization, security, logging).

💡 **Why Proxy?**  
- To control access to an object, e.g., to add **security checks** or **logging**.  
- **Optimizes resource usage** by controlling when an object is initialized or accessed.

✅ **Example:**  
Imagine a proxy that **controls access** to a sensitive `RealSubject` object, only allowing access to authorized users.

```python
class RealSubject:
    def request(self):
        return "RealSubject Request"

class Proxy:
    def __init__(self, real_subject: RealSubject):
        self.real_subject = real_subject

    def request(self):
        print("Proxy: Checking access...")
        return self.real_subject.request()

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())  # ✅ Proxy controls access to RealSubject
```
🎯 **Where is this used?**  
- **Security (access control)**.  
- **Lazy loading (load data only when needed)**.

---

### ** Structural Patterns in Real-World Systems**

| **Pattern** | **Use Case** | **Example** |
|-------------|--------------|-------------|
| **Adapter** | Converts one interface into another | Legacy system integration |
| **Bridge** | Decouples abstraction and implementation | UI frameworks with themes |
| **Composite** | Treats individual objects and compositions uniformly | File systems, component trees |
| **Decorator** | Adds responsibilities to objects dynamically | Dynamic logging, adding features to objects |
| **Facade** | Simplifies complex systems | Video conversion, complex library APIs |
| **Flyweight** | Reuses shared objects for memory efficiency | Text editors, image rendering |
| **Proxy** | Controls access to objects | Lazy initialization, access control |



### **Behavioral Design Patterns (LLD Interview Explanation)**

📌 **Definition:**  
Behavioral design patterns are focused on **how objects interact with each other** and **how responsibilities are assigned** within an application. These patterns help to define **communication patterns** and **behavioral relationships** between classes and objects, ensuring that they work **efficiently** and **flexibly**.

📌 **Why are Behavioral Patterns Important?**  
- They **define communication** and control the flow of **data** and **requests** between objects.
- Help manage the **complexity** of interactions in a system.
- Make the system **more flexible** and easier to **maintain**.

---

### **Common Behavioral Design Patterns:**
1. **Chain of Responsibility**
2. **Command**
3. **Interpreter**
4. **Iterator**
5. **Mediator**
6. **Memento**
7. **Observer**
8. **State**
9. **Strategy**
10. **Template Method**
11. **Visitor**

---

### **1️⃣ Chain of Responsibility → Passing Requests Along a Chain of Handlers**
📌 **Use Case:**  
The **Chain of Responsibility Pattern** allows multiple objects to **handle a request**, without the sender needing to know which object will handle it. The request is passed along a **chain** until it is handled by the appropriate object.

💡 **Why Chain of Responsibility?**  
- To **decouple** the sender and receiver of a request.
- Helps when there are **multiple possible handlers** for a request.

✅ **Example:**
Imagine a **logging system** where logs are handled differently based on **severity levels** (Info, Warning, Error).

```python
class Logger:
    def set_next(self, next_handler):
        self.next_handler = next_handler

    def handle(self, request):
        pass  # Abstract method

class InfoLogger(Logger):
    def handle(self, request):
        if request == "info":
            return "Handling info log"
        elif self.next_handler:
            return self.next_handler.handle(request)

class ErrorLogger(Logger):
    def handle(self, request):
        if request == "error":
            return "Handling error log"
        elif self.next_handler:
            return self.next_handler.handle(request)

# Usage
info_logger = InfoLogger()
error_logger = ErrorLogger()

info_logger.set_next(error_logger)

print(info_logger.handle("error"))  # ✅ Handling error log
print(info_logger.handle("info"))   # ✅ Handling info log
```
🎯 **Where is this used?**  
- **Event handling** in GUIs.
- **Middleware** in web applications (request handling, logging, authentication).

---

### **2️⃣ Command Pattern → Encapsulate Requests as Objects**
📌 **Use Case:**  
The **Command Pattern** is used to **encapsulate a request as an object**, allowing you to parameterize clients with different requests, queue requests, and log the requests.

💡 **Why Command?**  
- Provides **decoupling** between sender and receiver.
- Useful for **undo/redo operations**, transactional behavior, or queuing requests.

✅ **Example:**
Imagine a **remote control** for a smart home, where each button corresponds to a specific command (turn on lights, lock door).

```python
class Command:
    def execute(self):
        pass  # Abstract method

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return f"Turning on {self.light}"

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        return self.command.execute()

# Usage
light_command = LightOnCommand("Living Room Light")
remote = RemoteControl()
remote.set_command(light_command)
print(remote.press_button())  # ✅ Turning on Living Room Light
```
🎯 **Where is this used?**  
- **GUI applications** (button clicks, keyboard events).
- **Smart home automation** (remote control of devices).

---

### **3️⃣ Interpreter Pattern → Define Grammar for a Language**
📌 **Use Case:**  
The **Interpreter Pattern** is used to define a **grammar** for interpreting expressions and **evaluating the rules**.

💡 **Why Interpreter?**  
- Useful for building **interpreters** or **parsers** for domain-specific languages (DSLs), such as SQL, math expressions, or custom configuration files.

✅ **Example:**
Imagine a **simple arithmetic expression evaluator**.

```python
class Expression:
    def interpret(self):
        pass  # Abstract method

class NumberExpression(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self):
        return self.number

class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

# Usage
expr = AddExpression(NumberExpression(5), NumberExpression(3))
print(expr.interpret())  # ✅ 8
```
🎯 **Where is this used?**  
- **Custom scripting languages** (SQL parsers, Regex engines).
- **Mathematical expression evaluation** (simple calculators).

---

### **4️⃣ Iterator Pattern → Sequential Access to Elements**
📌 **Use Case:**  
The **Iterator Pattern** provides a way to **sequentially access elements** of an aggregate object (like a list or collection) without exposing the underlying representation.

💡 **Why Iterator?**  
- Simplifies **traversing** through collections (e.g., lists, sets).
- Ensures **encapsulation** of collection data while allowing iteration.

✅ **Example:**
Imagine you have a **book collection** and want to iterate over it without exposing the internal structure.

```python
class Book:
    def __init__(self, title):
        self.title = title

class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book.title
        else:
            raise StopIteration

# Usage
books = [Book("Book 1"), Book("Book 2"), Book("Book 3")]
iterator = BookIterator(books)

for book in iterator:
    print(book)  # ✅ Book 1, Book 2, Book 3
```
🎯 **Where is this used?**  
- **Data structures** (linked lists, trees).
- **Web frameworks** (pagination of search results).

---

### **5️⃣ Mediator Pattern → Centralized Communication Between Objects**
📌 **Use Case:**  
The **Mediator Pattern** defines an object that **coordinates communication** between objects, preventing direct interactions between them.

💡 **Why Mediator?**  
- To reduce **coupling** between components and promote **centralized control** of communication.

✅ **Example:**
Imagine a **chat room** where users communicate with each other through a mediator.

```python
class Mediator:
    def send(self, message, user):
        pass  # Abstract method

class ChatRoomMediator(Mediator):
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def send(self, message, user):
        for u in self.users:
            if u != user:
                u.receive(message)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.register_user(self)

    def send(self, message):
        print(f"{self.name}: {message}")
        self.mediator.send(message, self)

    def receive(self, message):
        print(f"{self.name} received: {message}")

# Usage
mediator = ChatRoomMediator()
user1 = User("User 1", mediator)
user2 = User("User 2", mediator)

user1.send("Hello!")  # ✅ User 1: Hello!  User 2 received: Hello!
user2.send("Hi!")     # ✅ User 2: Hi!  User 1 received: Hi!
```
🎯 **Where is this used?**  
- **GUI applications** (dialog boxes, form submissions).
- **Chat systems** (group chat, notifications).

---

### **6️⃣ Observer Pattern → Notify Objects of State Changes**
📌 **Use Case:**  
The **Observer Pattern** allows an object (subject) to notify a set of **dependent objects (observers)** when its state changes.

💡 **Why Observer?**  
- To allow for **dynamic subscriptions** and **loose coupling** between the subject and its observers.

✅ **Example:**
Imagine a **weather station** that notifies multiple display screens whenever there’s a change in the temperature.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass  # Abstract method

class TemperatureDisplay(Observer):
    def update(self, message):
        print(f"Temperature Display: {message}")

# Usage
subject = Subject()
temp_display = TemperatureDisplay()
subject.add_observer(temp_display)

subject.notify("Temperature: 25°C")  # ✅ Temperature Display: Temperature: 25°C
```
🎯 **Where is this used?**  
- **Event-driven systems** (UI updates, sensor networks).
- **Stock market systems** (notifying subscribers of price changes).

---

### **7️⃣ State Pattern → Change Behavior Based on State**
📌 **Use Case:**  
The **State Pattern** allows an object to **change its behavior** when its internal state changes, allowing different states to trigger **different actions**.

💡 **Why State?**  
- To **manage state transitions** and **avoid complex conditionals**.

✅ **Example:**
Imagine a **traffic light** that changes its behavior based on its state (Green, Yellow, Red).

```python
class State:
    def handle(self):
        pass  # Abstract method

class GreenState(State):
    def handle(self):
        return "Traffic light is green, cars go!"

class RedState(State):
    def handle(self):
        return "Traffic light is red, cars stop!"

class TrafficLight:
    def __init__(self):
        self.state = GreenState()

    def set_state(self, state):
        self.state = state

    def show(self):
        return self.state.handle()

# Usage
light = TrafficLight()
print(light.show())  # ✅ Traffic light is green, cars go!
light.set_state(RedState())
print(light.show())  # ✅ Traffic light is red, cars stop!
```
🎯 **Where is this used?**  
- **Game development** (character states, level transitions).
- **Workflow management systems** (task states, approval processes).

---

### **8️⃣ Strategy Pattern → Define a Family of Algorithms**
📌 **Use Case:**  
The **Strategy Pattern** defines a **family of algorithms** and allows the client to choose the appropriate algorithm at runtime.

💡 **Why Strategy?**  
- To **avoid hardcoding behavior** in a class and make it **easy to change or add new algorithms**.

✅ **Example:**
Imagine an **e-commerce checkout** process that allows **multiple discount strategies** (percentage discount, fixed amount discount).

```python
class DiscountStrategy:
    def apply(self, price):
        pass  # Abstract method

class PercentageDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.9  # 10% discount

class FixedAmountDiscount(DiscountStrategy):
    def apply(self, price):
        return price - 50  # $50 discount

class Checkout:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def calculate_total(self, price):
        return self.discount_strategy.apply(price)

# Usage
checkout = Checkout(PercentageDiscount())
print(checkout.calculate_total(200))  # ✅ 180.0

checkout.discount_strategy = FixedAmountDiscount()
print(checkout.calculate_total(200))  # ✅ 150.0
```
🎯 **Where is this used?**  
- **Pricing systems** (different discount strategies).  
- **Payment gateways** (different algorithms for payment processing).

---

### **Summary of Behavioral Patterns in Real-World Systems**

| **Pattern** | **Use Case** | **Example** |
|-------------|--------------|-------------|
| **Chain of Responsibility** | Multiple handlers for a request | Event handling, request processing |
| **Command** | Encapsulate a request as an object | Remote controls, undo/redo operations |
| **Interpreter** | Define grammar and interpret expressions | SQL parsers, regex engines |
| **Iterator** | Sequentially access elements | Collection traversal, pagination |
| **Mediator** | Centralized communication control | Chat systems, form submissions |
| **Memento** | Capture and restore object state | Undo/redo, backup systems |
| **Observer** | Notify objects of state changes | Event-driven systems, stock updates |
| **State** | Change behavior based on state | Game states, workflow systems |
| **Strategy** | Define a family of algorithms | Checkout discounts, payment processors |
| **Template Method** | Define the skeleton of an algorithm | Web frameworks, data processing pipelines |
| **Visitor** | Perform operations on elements of an object structure | AST manipulation, UI element traversal |




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