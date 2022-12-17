# Создать функцию с двумя обязательными аргументами (фамилия ученика, название предметы).
# В функции должен находиться словарь вида {‘фамилия’: {‘предмет1’:[оценки], ‘предмет2’:[оценки]}}.
# В словаре должно быть 3 ученика, у каждого ученика должно быть 4 предмета и 5 оценок. Пользователю должен
# предоставляться выбор (1 - вывод всех оценок по предмету у ученика, 2 - вывод среднего балла по этому предмету).
# Реализовать каждый из вариантов.

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

    def get_student_rating(surname: str, subject: str) -> str:

        user_input: str = input(
            "What do you want to know? All grades or average of them?\n HINT: type only 'all' or 'average'\n"
            " EXAMPLE: all\n"
        )
        prefix = f"Student - {surname}, subject - {subject}\n"
        result = data[surname][subject]

        if user_input.lower() == "all":
            result = result

        elif user_input.lower() == "average":
            result = sum(result) / len(result)

        else:
            result = {"Error": "you typed something wrong"}

        return prefix + str(result)

    #TODO проверять здесь
    print(get_student_rating("Sidorov", "English"))


if __name__ == "__main__":
    main()
