
students = []

print("Welcome to the Student Data Organizer!\n")

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("\nEnter student details:")

            student_id = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ")

            student = {
                "ID": student_id,
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": dob,
                "Subjects": subjects
            }

            students.append(student)

            print("\nStudent added successfully!")

        case 2:
            print("\n--- Display All Students ---")

            if not(students):
                print("No students found.")
            else:
                for s in students:
                    print(
                    print(f"Student ID: {s['ID']} | "
                        f"Name: {s['Name']} | "
                        f"Age: {s['Age']} | "
                        f"Grade: {s['Grade']} | "
                        f"Subjects: {s['Subjects']}")
                    )

        case 3:
            sid = input("Enter Student ID to update: ")

            for s in students:
                if s["ID"] == sid:
                    s["Name"] = input("New Name: ")
                    s["Age"] = int(input("New Age: "))
                    s["Grade"] = input("New Grade: ")
                    print("Student updated successfully!")
                    break
            else:
                print("Student not found.")

        case 4:
            sid = input("Enter Student ID to delete: ")

            for s in students:
                if s["ID"] == sid:
                    students.remove(s)
                    print("Student deleted successfully!")
                    break
            else:
                print("Student not found.")

        case 5:
            print("\n--- Subjects Offered ---")

            all_subjects = []

            for s in students:
                subject_list = s["Subjects"].split(",")

                for sub in subject_list:
                    sub = sub.strip()
                    if sub not in all_subjects:
                        all_subjects.append(sub)

            if len(all_subjects) == 0:
                print("No subjects available.")
            else:
                for sub in all_subjects:
                    print(sub)

        case 6:
            print("Exiting Program...")
            break

        case _:
            print("Invalid choice. Please try again.")
