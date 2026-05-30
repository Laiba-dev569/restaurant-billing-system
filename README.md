# hotel menu billing system project
# 🍽️ Python Restaurant Ordering System

A lightweight, interactive command-line interface (CLI) application built with Python. This program displays a digital menu, allows customers to add multiple items with custom quantities, tracks orders in real time, and generates a formatted bill receipt.

---

## ✨ Features

* **Dynamic Menu Generation:** Automatically reads and aligns menu items and prices.
* **Smart Input Sanitization:** Handles mixed casing (e.g., `pizza`, `PIZZA`, `Pizza`) seamlessly using string methods.
* **Multi-Item Cart:** Allows users to continuously add items and custom quantities to their tab.
* **Error Prevention:** Alerts users instantly if an item typed is not on the menu.
* **Clean Receipt Output:** Summarizes the final total cost neatly at the end of the session.

---

## 📋 Menu & Pricing Reference

| Dish / Drink | Price |
| :--- | :--- |
| Pizza | $40 |
| Pasta | $50 |
| Burger | $60 |
| Salad | $70 |
| Coffee | $80 |
| Tea | $90 |

---

## 🚀 How to Run the App

### Prerequisites
Ensure you have **Python 3.x** installed. Check your version by running:
```bash
python --version  
Welcome to Our Restaurant 🍽️
Here is our Menu:

Pizza      - $40
Pasta      - $50
Burger     - $60
Salad      - $70
Coffee     - $80
Tea        - $90

Enter item you want to order: Burger
Enter quantity: 2
2 x Burger added to your order ✔

Do you want to add more items? (yes/no): yes

Enter item you want to order: Coffee
Enter quantity: 1
1 x Coffee added to your order ✔

Do you want to add more items? (yes/no): no

========== BILL RECEIPT ==========
Total Amount to Pay: $200
Thank you for visiting! 😊
==================================
Data Structure: Uses a Python dictionary for the menu, making it incredibly easy to add or adjust prices.

Looping Mechanism: Uses a while True loop to keep the ordering session active until the user explicitly types anything other than yes.

Methods Used: * .strip() removes accidental trailing or leading spaces.

.title() ensures inputs match the capitalized keys in the dictionary.
