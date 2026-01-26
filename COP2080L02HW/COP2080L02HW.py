##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
grades = {}

# Loop until the user chooses to quit.
while True:

    # Ask user for action and convert to uppercase
    choice = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()

    # Add a new student
    if choice == "A":
        name = input("Enter the name of the student: ")

        if name in grades:
            print("Sorry, that student is already present.")
        else:
            grade = input("Enter the student's grade: ")

            if grade.isdigit() and 0 <= int(grade) <= 100:
                grades[name] = int(grade)
            else:
                print("Please enter grade as number 0-100")

    # Remove a student
    elif choice == "R":
        name = input("What student do you want to remove? ")

        if name in grades:
            grades.pop(name)
        else:
            print("Sorry, that student doesn't exist and couldn't be removed.")

    # Modify a student grade
    elif choice == "M":
        name = input("Enter the name of the student to modify: ")

        if name in grades:
            print("The old grade is", grades[name])
            grade = input("Enter the new grade: ")

            if grade.isdigit() and 0 <= int(grade) <= 100:
                grades[name] = int(grade)
            else:
                print("Please enter grade as number 0-100")
        else:
            print("Sorry, that student doesn't exist and couldn't be modified.")

    # Print average and all grades
    elif choice == "P":
        if len(grades) == 0:
            print("The average grade is 0")
        else:
            average = sum(grades.values()) / len(grades)
            print("The average grade is", average)

        for student in grades:
            print(student, ":", grades[student])

    # Quit program
    elif choice == "Q":
        print("Goodbye!")
        break

    # Invalid input
    else:
        print("Sorry, that wasn't a valid choice.")
