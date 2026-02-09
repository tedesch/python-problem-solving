## Converts a letter grade to a number (4-point scale)
## +0.3 for '+' and -0.3 for '-'
def gradeToNumber(g):
    g = g.strip().upper()

    # Base letter grade value
    letter = g[0]
    if letter == 'A':
        result = 4.0
    elif letter == 'B':
        result = 3.0
    elif letter == 'C':
        result = 2.0
    elif letter == 'D':
        result = 1.0
    elif letter == 'F':
        result = 0.0
    else:
        return None  # invalid

    # Adjust for + or - (F cannot have +/-)
    if len(g) == 2 and letter != 'F':
        if g[1] == '+':
            result += 0.3
        elif g[1] == '-':
            result -= 0.3

    # Keep in range
    if result > 4.0:
        result = 4.0
    if result < 0.0:
        result = 0.0

    return result


## Converts a number back to a letter grade
def numberToGrade(p):
    if p > 4.0:
        p = 4.0
    if p < 0.0:
        p = 0.0

    # Note: the thresholds here are designed to match the gradeToNumber function, so that converting a letter to a number
    # and back gives you the same letter
    if p >= 3.85:
        return "A"
    elif p >= 3.50:
        return "A-"
    elif p >= 3.15:
        return "B+"
    elif p >= 2.85:
        return "B"
    elif p >= 2.50:
        return "B-"
    elif p >= 2.15:
        return "C+"
    elif p >= 1.85:
        return "C"
    elif p >= 1.50:
        return "C-"
    elif p >= 1.15:
        return "D+"
    elif p >= 0.85:
        return "D"
    elif p >= 0.50:
        return "D-"
    else:
        return "F"


## Finds the index of the lowest number in a list
def lowestIndex(nums):
    low_i = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[low_i]:
            low_i = i
    return low_i


## Returns True if all 3 grades are B- or lower
def allBMinusOrLower(three_points):
    b_minus = gradeToNumber("B-")
    return (three_points[0] <= b_minus and
            three_points[1] <= b_minus and
            three_points[2] <= b_minus)


## Creates a 40-character wide ASCII box
def asciiBox40(lines):
    width = 40
    inside = width - 2
    top = "+" + "-" * inside + "+"
    out = [top]
    for line in lines:
        out.append("|" + line[:inside].ljust(inside) + "|")
    out.append(top)
    return "\n".join(out)