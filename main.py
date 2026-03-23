import random


def get_student_names() -> list[str]:
    students = []

    while True:
        student_name = input("Enter student name (q to quit): ").lower()
        if student_name == "q":
            break
        students.append(student_name)

    print("All students added")

    return students


def list_shuffle(arr: list, times: int) -> list:
    for i in range(times+1):
        random.shuffle(arr)
    return arr


def print_students(students: list[str], start_from: int = 0) -> None:
    for i, student in enumerate(students):
        print(f"{i+start_from + 1}. {student}")


print("Enter students with debt:")
students_with_debt = list_shuffle(get_student_names(), 33)

print("Enter other students:")
other_students = list_shuffle(get_student_names(), 33)

print("\n\nPriority – students with debt")
print(f"Final order of students:")
print_students(students_with_debt)
print("===OTHER STUDENTS===")
print_students(other_students, len(students_with_debt))





