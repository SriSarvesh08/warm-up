import csv
import json
try:
    students = []

    with open("day2/students.csv", "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty or has no headers.")

        reader.fieldnames = [header.strip() for header in reader.fieldnames]

        if "name" not in reader.fieldnames or "marks" not in reader.fieldnames:
            raise ValueError("CSV must contain name and marks columns.")

        for line_number, row in enumerate(reader, start=2):
            name = (row.get("name") or "").strip()
            raw_marks = (row.get("marks") or "").strip()

            if not name:
                raise ValueError(f"Missing student name at line {line_number}.")

            try:
                marks = float(raw_marks)
            except ValueError:
                raise ValueError(f"Invalid marks at line {line_number}.")

            if not 0 <= marks <= 100:
                raise ValueError(f"Marks must be between 0 and 100 at line {line_number}.")

            students.append({"name": name, "marks": marks})

    if not students:
        raise ValueError("No student records found.")
    
    total_students = len(students)
    average_marks = sum(s["marks"] for s in students) / total_students
    topper = max(students, key=lambda s: s["marks"])
    lowest = min(students, key=lambda s: s["marks"])
    passed = sum(1 for s in students if s["marks"] >= 50)
    failed = total_students - passed
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
    with open("day2/summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)
    print("Summary created successfully!")
except FileNotFoundError:
    print("Error: students.csv was not found. Check the file path.")

except PermissionError:
    print("Error: Permission denied while accessing a file.")
except (ValueError, OSError) as error:
    print(f"Error: {error}")
finally:
    print("File processing finished.")
