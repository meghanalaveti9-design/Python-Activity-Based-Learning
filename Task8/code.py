eligible = []

for i in range(3):
    print("\nApplicant", i + 1)
    name = input("Name: ")
    marks = []
    for subject in ["Subject 1", "Subject 2", "Subject 3"]:
        mark = float(input(subject + " mark: "))
        if mark < 0 or mark > 100:
            print("Marks must be from 0 to 100.")
            raise SystemExit
        marks.append(mark)
    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income (Rs.): "))

    if attendance < 0 or attendance > 100 or income < 0:
        print("Invalid attendance or income.")
        raise SystemExit

    average = sum(marks) / len(marks)
    if average >= 75 and min(marks) >= 60 and attendance >= 75 and income <= 300000:
        eligible.append((name, average, attendance))
        print(name, "is eligible.")
    else:
        print(name, "is not eligible.")

eligible.sort(key=lambda applicant: (applicant[1], applicant[2]), reverse=True)

print("\nSCHOLARSHIP RANKING")
if not eligible:
    print("No eligible applicants.")
else:
    for rank, applicant in enumerate(eligible, start=1):
        name, average, attendance = applicant
        print(rank, name, "| Average:", round(average, 2),
              "| Attendance:", attendance, "%")
