# ---------------- MENU ----------------
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
    'Tea': 90
}

# ---------------- WELCOME ----------------
print("\nWelcome to Our Restaurant 🍽️")
print("Here is our Menu:\n")

for item, price in menu.items():
    print(f"{item:<10} - ${price}")

# ---------------- ORDER SYSTEM ----------------
order_total = 0

while True:
    item = input("\nEnter item you want to order: ").strip().title()

    if item in menu:
        quantity = int(input("Enter quantity: "))
        order_total += menu[item] * quantity
        print(f"{quantity} x {item} added to your order ✔")
    else:
        print("Sorry, item not available ❌")

    another = input("Do you want to add more items? (yes/no): ").strip().lower()
    if another != "yes":
        break

# ---------------- BILL ----------------
print("\n========== BILL RECEIPT ==========")
print(f"Total Amount to Pay: ${order_total}")
print("Thank you for visiting! 😊")
print("==================================")