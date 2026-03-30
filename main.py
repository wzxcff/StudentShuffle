import random
import json
import datetime


def get_student_names() -> list[dict]:
    with open("students.json") as file:
        data = json.load(file)
    return [student for student in data["students"] if student['active']]


def form_priority(students: list[dict]) -> dict:
    debtors = [student for student in students if student['debt']]
    today_ready = [student for student in students if student['today_ready']]

    random.shuffle(debtors)
    random.shuffle(today_ready)

    return {
        'debtors': debtors,
        'today_ready': today_ready
    }


def print_students(students: list[dict], start_from: int = 0) -> None:
    for i, student in enumerate(students):
        print(f"{i+start_from + 1}. {student['name']}")


def main():
    seed = input("Set seed if you want to, leave blank to skip: ")
    if not seed:
        seed = datetime.date.today().strftime("%Y%m%d")

    random.seed(int(seed))

    print(f"Shuffling student with the current seed: {seed}")

    priority = form_priority(get_student_names())

    print("\nStudents with debt (PRIORITY):")
    print_students(priority['debtors'])
    print("\nStudents ready for today:")
    print_students(priority['today_ready'], len(priority['debtors']))


if __name__ == '__main__':
    main()





