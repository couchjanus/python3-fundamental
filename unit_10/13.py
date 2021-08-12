# Словарь ID=Баланс
accounts = {"John Doe": 100}
print(accounts)

try:
    make_call(accounts, "John Doe", mins=4, costs_per_min=2)
except Exception as e:
    print("Во время списывания стоимости звонка произошла ошибка:", e)

print(accounts)


# Совместное использование исключений и утверждений

weekday_names = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}

def weekday_name(weekday):
    """Вернуть название дня недели. Нумерация с 1.

    Параметры:
        weekday (int): номер дня недели.

    Исключения:
        - TypeError: 'weekday' не int;
        - ValueError: 'weekday' не число от 1 до 7.

    Результат:
        str: название дня недели.
    """
    # "Невозможная" ситуация - словарь 'weekday_names' может быть
    # "испорчен" - проверяется с помощью assert.
    assert weekday_names is not None and isinstance(weekday_names, dict), \
        "Внутренняя ошибка программы. Обратитесь в разрабочику."

    # Параметры функции проверяются с помощью исключений
    if not isinstance(weekday, int):
        raise TypeError("Параметр 'weekday' должен быть типа 'int'.")
    if weekday not in weekday_names:
        raise ValueError("Параметр 'weekday' должен быть целым числом "
                         "от 1 до 7.")

    return weekday_names[weekday]

# Блок try используется в любом случае т.к. может возникнуть ошибка
# независимо от того, используется пользовательский ввод,
# чтение данных из какого-либо источника или просто вызов функции

while True:
    try:
        weekday = int(input("Введите номер дня недели (1-7): "))

        # if not 1 <= weekday <= 7:
        #     raise ValueError("Номер дня недели должен быть целым числом "
        #                      "от 1 до 7.")

        # Раскомментируйте код ниже, чтобы получить срабатывание assert
        # weekday_names = None

        print("Это -", weekday_name(weekday))

        break
    except TypeError as err:
        print("Проверьте, что введено целое число.")
    except ValueError as err:
        print("Проверьте, что введено целое число, и оно "
              "находится в допустимых границах.")
    except Exception as err:
        print("Ошибка при определении названия дня недели.")
        print(err)  # Запись в лог информации об ошибке
