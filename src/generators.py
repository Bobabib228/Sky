"""
[
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'currency': 'USD', 'description': 'Покупка продуктов', 'amount': 100.5},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'currency': 'EUR', 'description': 'Оплата услуг', 'amount': 500.0}
]
"""
def filter_by_currency(trans: list, filter):
    for i in trans:
        if i['currency'] == filter:
            yield i

def transaction_descriptions(trans: list):
    for i in trans:
        yield i['description']

def card_number_generator(start, end):
    number = start
    for number in range(start, end+1):
        i = str(number)
        print(i)
        length = len(i)
        print(length)
        if length <= 16:
            card = ("0" * (16 - length)) + i
            yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:16]}"



