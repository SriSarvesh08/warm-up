
import csv
import json

students = []

# Read students.csv
with open("day2/students.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    print("CSV headers:", reader.fieldnames)

    for row in reader:
        students.append({
            "name": row["name"].strip(),
            "marks": float(row["marks"])
        })

# Check whether the file contains students
if not students:
    print("No student data found.")
else:
    marks_list = [student["marks"] for student in students]

    total_students = len(students)
    average_marks = sum(marks_list) / total_students

    topper = max(students, key=lambda s: s["marks"])
    lowest = min(students, key=lambda s: s["marks"])

    passed = sum(1 for mark in marks_list if mark >= 50)
    failed = total_students - passed

    # Create summary dictionary
    summary = {
        "total_students": total_students,
        "average_marks": round(average_marks, 2),
        "topper": topper["name"],
        "topper_marks": topper["marks"],
        "lowest_scorer": lowest["name"],
        "lowest_marks": lowest["marks"],
        "passed": passed,
        "failed": failed
    }

    # Write summary.json
    with open("summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print("Summary created successfully!")
    print(json.dumps(summary, indent=4))