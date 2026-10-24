items = {
    "Laptop": 50000,
    "Phone": 30000,
    "Tablet": 20000
}
highest=0
name=""
for item , price in items.items():
    if price>highest:
        highest=price
        name=item
print(name)