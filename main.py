from file_operations import read_csv_transactions2, read_excel_transactions
from generators import filter_by_currency, filter_by_currency_csv
from masks import get_mask_account, get_mask_card_number
from processing import filter_by_state, sort_by_date
from research import process_bank_search
from utils import load_transactions
from widget import get_date


def main():
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:""")
    while True:
        print("""
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла 
    """)
        user_ansfer = input()
        match user_ansfer:
            case "1":
                print("Для обработки выбран JSON-файл")
                while True:
                    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
                    user_ansfer = input()
                    if user_ansfer.lower() in ["executed", "canceled", "pending"]:
                        print(f"Операции отфильтрованы по статусу '{user_ansfer}'")
                        data = load_transactions("data/operations.json")
                        data = filter_by_state(data, f"{user_ansfer.upper()}")
                        while True:
                            print("Отсортировать операции по дате? Да/Нет")
                            user_ansfer = input()
                            if user_ansfer.lower() == "да":
                                while True:
                                    print("Отсортировать по возрастанию или по убыванию?")
                                    user_ansfer = input()
                                    if user_ansfer.lower() == "по убыванию":
                                        data = sort_by_date(data)
                                        break
                                    elif user_ansfer == "по возрастанию":
                                        data = sort_by_date(data, reverse=False)
                                        break
                                    elif user_ansfer.lower() != "по убыванию" and user_ansfer != "по возрастанию":
                                        print("Введите 'по убыванию' или 'по возрастанию'!")
                                        continue
                            elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                print("Введите 'да' или 'нет'!")
                                continue
                            while True:
                                print("Выводить только рублевые транзакции? Да/Нет")
                                user_ansfer = input()
                                if user_ansfer.lower() == "да":
                                    data = list(filter_by_currency(data, "RUB"))
                                elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                    print("Введите 'да' или 'нет'!")
                                    continue
                                while True:
                                    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                                    user_ansfer = input()
                                    if user_ansfer.lower() == "да":
                                        print("Введите слово для сортировки")
                                        user_ansfer = input()
                                        data = process_bank_search(data, user_ansfer)
                                    elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                        print("Введите 'да' или 'нет'!")
                                        continue
                                    print("Распечатываю итоговый список транзакций...")
                                    print(f"Всего банковских операций в выборке: {len(list(data))}")
                                    for item in data:
                                        if item != {}:
                                            date = get_date(item["date"])
                                            if "Перевод" in item["description"]:
                                                print(1)
                                                if "Счет" in item["to"]:
                                                    number_account_to = get_mask_account(item["to"])
                                                    types_to = "Счет"
                                                else:
                                                    number_account_to = get_mask_card_number(item["to"][-16:])
                                                    types_to = item["to"][:-17]
                                                if "Счет" in item["from"]:
                                                    number_account_from = get_mask_account(item["from"])
                                                    types_from = "Счет"
                                                else:
                                                    number_account_from = get_mask_card_number(item["from"][-16:])
                                                    types_from = item["from"][:-17]
                                                print(f"""
                                                {date} {item["description"]}
                                                {types_from} {number_account_from} --> {types_to} {number_account_to}
                                                Сумма: {item["operationAmount"]["amount"]}
                                                """)
                                            else:
                                                print(2)
                                                if "Счет" in item["to"]:
                                                    number_account = get_mask_account(item["to"])
                                                    types_to = "Счет"
                                                else:
                                                    number_account = get_mask_card_number(item["to"][-16:])
                                                    types_to = item["to"][:-17]
                                                print(f"""
                                                {date} {item["description"]}
                                                {types_to} {number_account}
                                                Сумма: {item["operationAmount"]["amount"]}
                                                """)
                                    break
                                break
                            break
                        break
                    else:
                        print(f"Статус операции '{user_ansfer}' недоступен")
            case "2":
                print("Для обработки выбран СSV-файл")
                while True:
                    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
                    user_ansfer = input()
                    if user_ansfer.lower() in ["executed", "canceled", "pending"]:
                        print(f"Операции отфильтрованы по статусу '{user_ansfer}'")
                        data = read_csv_transactions2("data/transactions.csv")
                        data = filter_by_state(data, f"{user_ansfer.upper()}")
                        while True:
                            print("Отсортировать операции по дате? Да/Нет")
                            user_ansfer = input()
                            if user_ansfer.lower() == "да":
                                while True:
                                    print("Отсортировать по возрастанию или по убыванию?")
                                    user_ansfer = input()
                                    if user_ansfer.lower() == "по убыванию":
                                        data = sort_by_date(data)
                                        break
                                    elif user_ansfer == "по возрастанию":
                                        data = sort_by_date(data, reverse=False)
                                        break
                                    elif user_ansfer.lower() != "по убыванию" and user_ansfer != "по возрастанию":
                                        print("Введите 'по убыванию' или 'по возрастанию'!")
                                        continue
                            elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                print("Введите 'да' или 'нет'!")
                                continue
                            while True:
                                print("Выводить только рублевые транзакции? Да/Нет")
                                user_ansfer = input()
                                if user_ansfer.lower() == "да":
                                    data = list(filter_by_currency_csv(data, "RUB"))
                                elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                    print("Введите 'да' или 'нет'!")
                                    continue
                                while True:
                                    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                                    user_ansfer = input()
                                    if user_ansfer.lower() == "да":
                                        print("Введите слово для сортировки")
                                        user_ansfer = input()
                                        data = process_bank_search(data, user_ansfer)
                                    elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                        print("Введите 'да' или 'нет'!")
                                        continue
                                    print("Распечатываю итоговый список транзакций...")
                                    print(f"Всего банковских операций в выборке: {len(list(data))}")
                                    for item in data:
                                        if item != {}:
                                            date = get_date(item["date"])
                                            if "Перевод" in item["description"]:
                                                print(1)
                                                if "Счет" in item["to"]:
                                                    number_account_to = get_mask_account(item["to"])
                                                    types_to = "Счет"
                                                else:
                                                    number_account_to = get_mask_card_number(item["to"][-16:])
                                                    types_to = item["to"][:-17]
                                                if "Счет" in item["from"]:
                                                    number_account_from = get_mask_account(item["from"])
                                                    types_from = "Счет"
                                                else:
                                                    number_account_from = get_mask_card_number(item["from"][-16:])
                                                    types_from = item["from"][:-17]
                                                print(f"""
                                                 {date} {item["description"]}
                                                 {types_from} {number_account_from} --> {types_to} {number_account_to}
                                                 Сумма: {item["amount"]}
                                                 """)
                                            else:
                                                print(2)
                                                if "Счет" in item["to"]:
                                                    number_account = get_mask_account(item["to"])
                                                    types_to = "Счет"
                                                else:
                                                    number_account = get_mask_card_number(item["to"][-16:])
                                                    types_to = item["to"][:-17]
                                                print(f"""
                                                {date} {item["description"]}
                                                {types_to} {number_account}
                                                Сумма: {item["amount"]}
                                                """)
                                    break
                                break
                            break
                        break
                    else:
                        print(f"Статус операции '{user_ansfer}' недоступен")
            case "3":
                print("Для обработки выбран СSV-файл")
                while True:
                    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
                    user_ansfer = input()
                    if user_ansfer.lower() in ["executed", "canceled", "pending"]:
                        print(f"Операции отфильтрованы по статусу '{user_ansfer}'")
                        data = read_excel_transactions("data/transactions_excel.xlsx")
                        data = filter_by_state(data, f"{user_ansfer.upper()}")
                        while True:
                            print("Отсортировать операции по дате? Да/Нет")
                            user_ansfer = input()
                            if user_ansfer.lower() == "да":
                                while True:
                                    print("Отсортировать по возрастанию или по убыванию?")
                                    user_ansfer = input()
                                    if user_ansfer.lower() == "по убыванию":
                                        data = sort_by_date(data)
                                        break
                                    elif user_ansfer == "по возрастанию":
                                        data = sort_by_date(data, reverse=False)
                                        break
                                    elif user_ansfer.lower() != "по убыванию" and user_ansfer != "по возрастанию":
                                        print("Введите 'по убыванию' или 'по возрастанию'!")
                                        continue
                            elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                print("Введите 'да' или 'нет'!")
                                continue
                            while True:
                                print("Выводить только рублевые транзакции? Да/Нет")
                                user_ansfer = input()
                                if user_ansfer.lower() == "да":
                                    data = list(filter_by_currency_csv(data, "RUB"))
                                elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                    print("Введите 'да' или 'нет'!")
                                    continue
                                while True:
                                    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                                    user_ansfer = input()
                                    if user_ansfer.lower() == "да":
                                        print("Введите слово для сортировки")
                                        user_ansfer = input()
                                        data = process_bank_search(data, user_ansfer)
                                    elif user_ansfer.lower() != "да" and user_ansfer.lower() != "нет":
                                        print("Введите 'да' или 'нет'!")
                                        continue
                                    print("Распечатываю итоговый список транзакций...")
                                    print(f"Всего банковских операций в выборке: {len(list(data))}")
                                    for item in data:
                                        if item != {}:
                                            date = get_date(item["date"])
                                            if "Перевод" in item["description"]:
                                                if "Счет" in item["to"]:
                                                    number_account_to = get_mask_account(item["to"])
                                                    types_to = "Счет"
                                                else:
                                                    number_account_to = get_mask_card_number(item["to"][-16:])
                                                    types_to = item["to"][:-17]
                                                if "Счет" in item["from"]:
                                                    number_account_from = get_mask_account(item["from"])
                                                    types_from = "Счет"
                                                else:
                                                    number_account_from = get_mask_card_number(item["from"][-16:])
                                                    types_from = item["from"][:-17]
                                                print(f"""
                                                {date} {item["description"]}
                                                {types_from} {number_account_from} --> {types_to} {number_account_to}
                                                Сумма: {item["amount"]}
                                                """)
                                            else:
                                                if "Счет" in item["to"]:
                                                    number_account = get_mask_account(item["to"])
                                                    types_to = "Счет"
                                                else:
                                                    number_account = get_mask_card_number(item["to"][-16:])
                                                    types_to = item["to"][:-17]
                                                print(f"""
                                                {date} {item["description"]}
                                                {types_to} {number_account}
                                                Сумма: {item["amount"]}
                                                """)
                                    break
                                break
                            break
                        break
                    else:
                        print(f"Статус операции '{user_ansfer}' недоступен")
            case _:
                print("Ответ не выбран")


main()
