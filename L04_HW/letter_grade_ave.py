from grade_compute import *

from grade_compute import (
    gradeToNumber,
    numberToGrade,
    lowestIndex,
    allBMinusOrLower,
    asciiBox40
)

## Validates the input line:
## allows 'Q' to quit
## otherwise requires 4 grades separated by $
def validateInput(line):
    if line is None:
        return False, "Empty input."

    line = line.strip()
    if line.upper() == "Q":
        return True, "Q"

    parts = line.split("$")
    if len(parts) != 4:
        return False, "Enter 4 grades separated by $ (ex: A$B+$C$A-)."

    grades = []
    for p in parts:
        g = p.strip().upper()
        pts = gradeToNumber(g)
        # gradeToNumber returns None if invalid
        if pts is None:
            return False, f"Invalid grade: {p.strip()}"
        # Block A+ since it's not allowed in this system
        if g == "A+":
            return False, "A+ is not allowed."
        grades.append(g)

    return True, grades


## Processes one line of input
def processLine():
    line = input("Enter 4 grades seperated by $ (or Q to quit): ").upper()

    ok, data = validateInput(line)
    if not ok:
        print("ERROR:", data)
        return False  # keep looping

    if data == "Q":
        return True  # signal quit

    grades = data
    points = [gradeToNumber(g) for g in grades]

    # Drop lowest grade
    lowestGrade = lowestIndex(points)
    dropped_grade = grades[lowestGrade]

    three_points = []
    for i in range(4):
        if i != lowestGrade:
            three_points.append(points[i])

    calc_avg = sum(three_points) / 3

    # Curve bonus rule
    final_avg = calc_avg
    if allBMinusOrLower(three_points):
        final_avg += 0.25

    if final_avg > 4.0:
        final_avg = 4.0

    final_letter = numberToGrade(final_avg)

    # ASCII output (40 wide)
    lines = [
        "GRADE REPORT SUMMARY".center(38),
        "-" * 38,
        "Grades Entered: " + ", ".join(grades),
        "Lowest Grade Dropped: " + dropped_grade,
        "Calculated Average: " + f"{final_avg:.2f}",
        "Final Letter Grade: " + final_letter
    ]

    print(asciiBox40(lines))
    return False  # keep looping


## Main loop using a flag to control when to quit
def main():
    flag = False
    while flag == False:
        flag = processLine()


main()