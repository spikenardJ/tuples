# Question 3: Mastering Tuple Packing and Unpacking in Python

# Task 1: Customer Order Processing

import sys
from termcolor import colored

def add_new_customer_order(orders):
    for new_order in orders:
        customer_name = input("Enter the name of the customer: ").title()
        product_ordered = input(f"Enter the product that {customer_name} ordered: ").title()
        quantity = input(f"Enter the quantity of {product_ordered} that {customer_name} ordered: ")
        new_order = (customer_name, product_ordered, quantity)

        if new_order in orders:
            print("This order already exists.")
            return
        else:
            orders.append((new_order))
            print(f"{customer_name}'s {product_ordered}(s) has been added to orders successfully.")
            return

def display_customer_orders(orders):
    print("")
    found = False
    for i, (name, product, quantity) in enumerate(orders):
        print(colored(f"\nOrder {i + 1}:", attrs=["bold"])) 
        print("Customer Name: ", name, " \nProduct: ", product, " \nQuantity: ", quantity)
        found = True
    if not found:
        print("There are no orders yet.")

def main():
    orders = [
        ("Alice", "Laptop", 1),
        ("Bob", "Camera", 2),
        ("John", "iPhone", 1),
        ("Mike", "iPad", 1),
        ("Elizabeth", "Phone Charger", 4)
    ]

    while True:
        print("\n1. Add new customer order")
        print("2. display all customer orders")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_customer_order(orders)
        elif choice == "2":
            display_customer_orders(orders)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()