def get_marks():
    marks = []

    while True:
        mark = input("Enter Mark (or type 'done' to finish): ")

        if mark.lower() == "done":
            break

        marks.append(float(mark))

    return marks

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    elif avg >= 50:
        return "E"
    else:
        return "F"


def display_result(name, marks):
    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    print("\n----- Student Report -----")
    print("Student Name :", name)
    print("Marks        :", marks)
    print("Average      :", round(average, 2))
    print("Grade        :", grade)


def main():
    name = input("Enter Student Name: ")
    marks = get_marks()
    display_result(name, marks)


main()