def calculate_bill(units):
    if units < 0:
        return -1
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    surcharge = energy * 0.05
    bill = energy + 50 + surcharge
    if units <= 100:
        bill -= 20
    return bill

month1 = int(input("Enter units used in Month 1: "))
month2 = int(input("Enter units used in Month 2: "))

bill1 = calculate_bill(month1)
bill2 = calculate_bill(month2)

if bill1 < 0 or bill2 < 0:
    print("Invalid units. Units cannot be negative.")
else:
    print("Month 1 bill: Rs.", round(bill1, 2))
    print("Month 2 bill: Rs.", round(bill2, 2))
    difference = bill2 - bill1
    print("Bill difference: Rs.", round(abs(difference), 2))
    if difference > 0:
        print("Bill increased in Month 2.")
    elif difference < 0:
        print("Bill decreased in Month 2.")
    else:
        print("Both bills are equal.")
