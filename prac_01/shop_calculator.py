items_amount = int(input("Number of items: "))
total_price = 0
count = 1
while items_amount < 0:
    print("Invalid amount")
    items_amount = int(input("Number of items: "))

for items in range(items_amount):
    price = float(input(f"Price of item {count}: $"))
    total_price = total_price + price
    count = count + 1

if total_price > 100:
    total_price = total_price - (0.1 * total_price)

print(f"Total price for {items_amount} items is ${total_price:.2f}")
