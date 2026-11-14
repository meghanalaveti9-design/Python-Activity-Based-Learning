items = []
subtotal = 0
tax_total = 0

for i in range(3):
    print("\nProduct", i + 1)
    name = input("Product name: ")
    category = input("Category (electronics/other): ").lower()
    price = float(input("Price: Rs. "))
    quantity = int(input("Quantity: "))
    if price < 0 or quantity < 0:
        print("Invalid price or quantity.")
        raise SystemExit
    items.append((name, category, price, quantity))
    subtotal += price * quantity

if subtotal >= 2000:
    discount = min(subtotal * 0.10, 500)
else:
    discount = 0

discount_ratio = discount / subtotal if subtotal > 0 else 0
print("\nITEMIZED INVOICE")
for name, category, price, quantity in items:
    item_total = price * quantity
    item_discount = item_total * discount_ratio
    taxable = item_total - item_discount
    rate = 0.10 if category == "electronics" else 0.05
    tax = taxable * rate
    tax_total += tax
    print(name, "| Qty:", quantity, "| Subtotal:", round(item_total, 2),
          "| Tax:", round(tax, 2))

print("Subtotal: Rs.", round(subtotal, 2))
print("Discount: Rs.", round(discount, 2))
print("Tax total: Rs.", round(tax_total, 2))
print("Final bill: Rs.", round(subtotal - discount + tax_total, 2))
