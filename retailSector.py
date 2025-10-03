# 1. Create dictionary
inventory = {
    "Shoes": 25,
    "Bags": 8,
    "Belts": 15,
    "Shirts": 12,
    "Hats": 5
}

# 2. Add new product & update quantity
inventory["Socks"] = 30
inventory["Bags"] = 10  # update

# 3. Function to return products with stock < 10
def low_stock_items(inv):
    return [item for item, qty in inv.items() if qty < 10]

print("Low stock:", low_stock_items(inventory))

# 4. Delete discontinued product
del inventory["Hats"]
print("Updated inventory:", inventory)

# 5. Loop through and print each product with quantity
for product, qty in inventory.items():
    print(f"{product}: {qty}")
