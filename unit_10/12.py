# Использование оператора assert для проверки входных и выходных данных

def make_call(accounts, account_id, mins, costs_per_min):
    """Списать со счета 'account' на 'value' баллов в случае звонка.

    Параметры:
        - accounts (dict): словарь со всеми счетами абонентов;
        - account_id (int): идентификатор абонента в словаре 'accounts';
        - mins (int): количество минут разговора;
        - costs_per_min (int): стоимость минуты разговора.
    """

    def get_costs(mins, costs_per_min):
        """Вернуть стоимость звонка.

        Параметры:
            - mins (int): количество минут разговора;
            - costs_per_min (int): стоимость минуты разговора.
        """
        return -mins * costs_per_min

    # Проверка типов
    assert isinstance(mins, int), "Параметр 'mins' имеет неверный тип!"
    assert isinstance(costs_per_min, (int, float)),\
        "Параметр 'costs_per_min' имеет неверный тип!"

    # Проверка значений
    assert mins > 0, "Параметр 'mins' должен быть > 0"
    assert costs_per_min >= 0, "Параметр 'costs' должен быть >= 0"

    # Расчет (стоимость звонка не должна быть меньше 0)
    costs_total = get_costs(mins, costs_per_min)
    assert costs_total >= 0,\
        "Расчет стоимости звонка был осуществлен неверно!"
    accounts[account_id] -= costs_total
