# Создать функцию с двумя обязательными аргументами (фамилия ученика, название предметы).
# В функции должен находиться словарь вида {‘фамилия’: {‘предмет1’:[оценки], ‘предмет2’:[оценки]}}.
# В словаре должно быть 3 ученика, у каждого ученика должно быть 4 предмета и 5 оценок. Пользователю должен
# предоставляться выбор (1 - вывод всех оценок по предмету у ученика, 2 - вывод среднего балла по этому предмету).
# Реализовать каждый из вариантов.
from typing import Dict

data = {
    "Ivanov": {
        "Math": [4, 5, 3, 4, 5],
        "Russian": [5, 5, 5, 4, 5],
        "English": [3, 3, 3, 4, 4],
        "Physics": [2, 3, 4, 4, 4],
    },
    "Petrov": {
        "Math": [3, 3, 2, 4, 3],
        "Russian": [5, 5, 4, 4, 5],
        "English": [4, 5, 4, 4, 5],
        "Physics": [3, 3, 3, 4, 5],
    },
    "Sidorov": {
        "Math": [2, 3, 4, 5, 2],
        "Russian": [4, 5, 4, 4, 5],
        "English": [4, 4, 4, 4, 4],
        "Physics": [4, 4, 3, 4, 3],
    }
}


def main():

    def get_student_rating() -> dict[str, str] | dict[str, str] | str:

        print(f"Our students - {[x for x in data]}")
        print(f"Our subjects - {[x for x in data['Ivanov']]}")

        student: str = input(
            "Choose student, type in his sirname\n"
        )
        if student not in data.keys():
            return {"Error": "you typed something wrong in surname"}

        subject: str = input(
            "Choose subject, type in any subject\n"
        )
        if subject not in data["Petrov"]:
            return {"Error": "you typed something wrong in subject"}

        user_input_info: str = input(
            "What do you want to know? All grades or average of them?\n HINT: type only 'all' or 'average'\n"
            " EXAMPLE: all\n"
        )
        if user_input_info not in ["all", "average"]:
            return {"Error": "you typed something wrong in action"}

        prefix = f"Student - {student}, subject - {subject}\n"
        result = data[student][subject]

        if user_input_info.lower() == "all":
            result = result

        elif user_input_info.lower() == "average":
            result = sum(result) / len(result)

        return prefix + str(result)

    print(get_student_rating())


if __name__ == "__main__":
    main()
