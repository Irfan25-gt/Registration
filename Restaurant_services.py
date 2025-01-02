# Define the menu of restaurant
menu = {
    'pizza': 60,
    'Pasta': 40,
    'Burger': 60,
    'salad': 70,
    'coffee': 80,
}

# Greet the user
print("Welcome to Python Restaurant")
print("pizza: 60 Rs\nPasta: 40 Rs\nBurger: 60 Rs\nsalad: 70 Rs\ncoffee: 80 Rs")

order_total = 0

# Start the ordering process
while True:
    item = input("Enter the name of the item you want to order: ").lower()  # Convert to lowercase for consistency

    if item in menu:
        order_total += menu[item]  # Add the price of the ordered item to the total
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available yet!")

    # Ask if the user wants to add another item
    another_order = input("Do you want to add another item? (yes/no): ").lower()
    if another_order != 'yes':
        break  # Exit the loop if the user doesn't want to order more items

# Print the total amount to pay
print(f"The total amount to pay is {order_total} Rs")