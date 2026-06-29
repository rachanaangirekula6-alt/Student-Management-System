students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        marks = input("Enter student marks: ")

        student = {
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(student)

    elif choice == "3":
        search = input("Enter student name: ")
        found = False

        for student in students:
            if student["name"].lower() == search.lower():
                print(student)
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        search = input("Enter student name: ")

        for student in students:
            if student["name"].lower() == search.lower():
                new_marks = input("Enter new marks: ")
                student["marks"] = new_marks
                print("Marks updated successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        search = input("Enter student name: ")

        for student in students:
            if student["name"].lower() == search.lower():
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")