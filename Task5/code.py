students = []
marks = []
subjects = ["Python", "Maths", "English"]

for i in range(3):
    name = input("Enter student name: ")
    row = []
    for subject in subjects:
        mark = float(input("Enter " + subject + " mark for " + name + ": "))
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            raise SystemExit
        row.append(mark)
    students.append(name)
    marks.append(row)

totals = []
print("\nSTUDENT REPORT")
for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    totals.append(total)
    print(students[i], "Total:", total, "Average:", round(average, 2))

print("\nSUBJECT AVERAGES")
low_subjects = []
for j in range(len(subjects)):
    total = 0
    for i in range(len(students)):
        total += marks[i][j]
    average = total / len(students)
    print(subjects[j], "average:", round(average, 2))
    if average < 40:
        low_subjects.append(subjects[j])

top_index = totals.index(max(totals))
print("Top performer:", students[top_index])
print("Low-average subjects:", low_subjects if low_subjects else "None")
