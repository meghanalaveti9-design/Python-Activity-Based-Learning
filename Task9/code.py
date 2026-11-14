rows = 4
columns = 4
reserved = [(0, 0), (1, 1)]
seats = [["EMPTY" for c in range(columns)] for r in range(rows)]

for r, c in reserved:
    seats[r][c] = "RESERVED"

names_text = input("Enter student names separated by commas: ")
students = names_text.split(",")
for i in range(len(students)):
    students[i] = students[i].strip()

student_index = 0
for r in range(rows):
    for c in range(columns):
        if (r, c) not in reserved and (r + c) % 2 == 0 and student_index < len(students):
            seats[r][c] = students[student_index]
            student_index += 1

print("\nSEATING ARRANGEMENT")
for r in range(rows):
    row_display = []
    for c in range(columns):
        row_display.append(seats[r][c])
    print("Row", r + 1, ":", " | ".join(row_display))

if student_index < len(students):
    print("Unseated students:", students[student_index:])
else:
    print("All students seated where permitted.")
