# List of items: each item is a dictionary with name, price, and quantity
items = [
    {"name": "Apple", "price": 0.5, "quantity": 4},
    {"name": "Bread", "price": 1.5, "quantity": 2},
    {"name": "Milk", "price": 2.0, "quantity": 1},
    {"name": "Eggs", "price": 0.2, "quantity": 12}
]

total_cost = 0.0  # Use float for currency

# Calculate total cost
for item in items:
    cost = item["price"] * item["quantity"]
    total_cost += cost
    print(f"{item['quantity']} x {item['name']} @ ${item['price']} each = ${cost:.2f}")

# Print total bill
print(f"\nTotal Bill: ${total_cost:.2f}")
