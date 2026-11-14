products = []

for i in range(3):
    print("\nProduct", i + 1)
    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    incoming = int(input("Incoming quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    actual = int(input("Actual closing stock: "))
    target = int(input("Target stock level: "))

    if min(opening, incoming, dispatched, actual, target) < 0:
        print("Stock values cannot be negative.")
        raise SystemExit
    if dispatched > opening + incoming:
        print("Warning: dispatched quantity exceeds available stock.")

    products.append((name, opening, incoming, dispatched, actual, target))

print("\nINVENTORY RECONCILIATION")
for name, opening, incoming, dispatched, actual, target in products:
    expected = opening + incoming - dispatched
    discrepancy = actual - expected
    replenishment = max(0, target - actual)
    print("\nProduct:", name)
    print("Expected closing stock:", expected)
    print("Actual closing stock:", actual)
    print("Discrepancy (actual - expected):", discrepancy)
    print("Replenishment required:", replenishment)
