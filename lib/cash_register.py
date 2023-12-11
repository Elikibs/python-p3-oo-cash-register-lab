#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for i in range(quantity):
            self.items.append(title)
        self.last_transaction = price

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            return f"Discount of {self.discount}% applied and the total discount is; {discount_amount}"
        else:
            return "No discount to apply."

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.items.pop()


# Create a cash register with a 10% discount
customer1 = CashRegister(10)

# Adds items to the cash register
customer1.add_item("eggs", 18.00)
customer1.add_item("sugar", 190.00, 2)
customer1.add_item("colgate", 65.50, 3)
print(f"Total before discount: {customer1.total}")

# Apply the discount
print(customer1.apply_discount())

# Before voiding the last transaction
print(f"Items list before removing last transcation; {customer1.items}")
print(f"Last transaction amount; {customer1.last_transaction}")

# Void the last transaction
customer1.void_last_transaction()
print(f"Items list after removing last transcation; {customer1.items}")

#Get the total price
print(f"The total price after discount and removing last transaction amount is KES {customer1.total:.2f}")

