students = {}

try:
 
    sid = input("Enter Student ID: ")
    grade = input("Enter Grade: ")

    if grade == "":
        raise ValueError("Grade cannot be empty")

    students[sid] = float(grade)

    uid = input("Enter ID to update: ")
    if uid not in students:
        raise KeyError("Invalid Student ID")

    new_grade = float(input("Enter new grade: "))
    students[uid] = new_grade

    did = input("Enter ID to delete: ")
    if did not in students:
        raise KeyError("Invalid Student ID")

    del students[did]

    print("Final Records:", students)

except ValueError:
    print("Type mismatch or empty grade input")
except KeyError as e:
    print(e)
except Exception as e:
    print("Error:", e)