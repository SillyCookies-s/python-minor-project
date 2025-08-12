students = {}
while True:
    print("1. Add 2. Update 3. Show 4. Exit")
    choice = input("Option: ")
    if choice == "1":
        name = input("Name: ")
        grade = input("Grade: ")
        students[name] = grade
    elif choice == "2":
        name = input("Name: ")
        if name in students:
            students[name] = input("Grade: ")
    elif choice == "3":
        for name, grade in students.items():
            print(name + ": " + grade)
    elif choice == "4":
        break