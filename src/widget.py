def mask_account_card(input_number: str) -> str:
    """
    Маскирует номер банковского счета или карты в зависимости от типа.

    Функция принимает строку, содержащую тип ('Счёт' или название карты) и номер.
    Для счета: отображаются первые 4 символа и последние 4 цифры, остальное скрывается звездочками.
    Для карты: отображаются название карты, первые 6 цифр (в формате XXXX XX** **** XXXX) и последние 4 цифры.

    """

    typ = input_number.split()

    if typ[0] == "Счёт":
        account_str = input_number

        return f"{account_str[:4]} **{account_str[-4:]}"
    else:
        Card_Name = typ[0]
        Card_Number = typ[1]
        return f"{Card_Name} {Card_Number[0:4]} {Card_Number[4:6]}** **** {Card_Number[-4:]}"


def get_date(input_date: str) -> str:
    """
    Форматирует дату, приводя ее в формат ДД.ММ.ГГ
    """
    return f"{input_date[8:10]}.{input_date[5:7]}.{input_date[0:4]}"
