attended = int(input("Classes attended: "))
conducted = int(input("Total classes conducted: "))
threshold = 75

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details.")
else:
    percentage = attended / conducted * 100
    print("Current attendance:", round(percentage, 2), "%")

    future = 0
    while (attended + future) / (conducted + future) * 100 < threshold:
        future += 1

    if future == 0:
        print("You already meet the attendance requirement.")
    else:
        print("Minimum consecutive classes to attend:", future)
        print("Attendance after attending them:",
              round((attended + future) / (conducted + future) * 100, 2), "%")
