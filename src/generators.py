def filter_by_currency(trans: list, filter):
    """
    Фильтрует банковские операции по валюте

    принимает на вход список словерей банковских операций и параметр фильтрации
    возвращает итерируемый объект
    """
    for i in trans:
        if i["currency"] == filter:
            yield i


def transaction_descriptions(trans: list):
    """
    Возвращает описание транзакций по очереди

    принимает список словарей с транзакциями
    возвращает итерируемый объект
    """
    for i in trans:
        yield i["description"]


def card_number_generator(start, end):
    """
    генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXX, где X — цифра номера карты
    принимает на вход стартовое и конечное значение
    возвращает номер банковской карты от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    number = start
    for number in range(start, end + 1):
        i = str(number)
        length = len(i)
        if length <= 16:
            card = ("0" * (16 - length)) + i
            yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:16]}"
