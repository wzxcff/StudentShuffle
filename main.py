import random
import json


def get_student_names() -> list[dict]:
    with open("students.json") as file:
        data = json.load(file)
    return [student for student in data["students"] if student['active']]


def list_shuffle(arr: list, times: int) -> list:
    for i in range(times+1):
        random.shuffle(arr)
    return arr


def form_priority(students: list[dict]) -> dict:
    res = {'debtors': list_shuffle([student for student in students if student['debt']], 55),
           'today_ready': list_shuffle([student for student in students if student['today_ready']], 55)}
    return res


def print_students(students: list[dict], start_from: int = 0) -> None:
    for i, student in enumerate(students):
        print(f"{i+start_from + 1}. {student['name']}")


def main():
    priority = form_priority(get_student_names())

    print("\nStudents with debt (PRIORITY):")
    print_students(priority['debtors'])
    print("\nStudents ready for today:")
    print_students(priority['today_ready'], len(priority['debtors']))


if __name__ == '__main__':
    main()





