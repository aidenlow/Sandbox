items = int(input("Please enter the amount of items"))
while items < 0:
    print("Number of items is not valid, try again")
    items = int(input("Please enter the amount of items"))
total = 0

for i in range(0, items, 1):
    itemPrice = float(input("Price of item"))
    total = total + itemPrice

if total > 100:
    total = total * 0.9

print("Total price for ",items, "items is $", total)