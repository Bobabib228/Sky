import datetime


def mask_account_card(input_number: str) -> str:

    typ = input_number.split()

    if typ[0] == "Счёт":
        account_str = input_number

        return f"{account_str[:4]} **{account_str[-4:]}"
    else:
        Card_Name = typ[0]
        Card_Number = typ[1]
        return f"{Card_Name} {Card_Number[0:4]} {Card_Number[4:6]}** **** {Card_Number[-4:]}"  # 1234 5678 9123 4567


def get_date(input_date: str) -> str:
    return f"{input_date[8:10]}.{input_date[5:7]}.{input_date[0:4]}"
