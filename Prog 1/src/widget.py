import datetime


def mask_account_card(input_number: str) -> str:

    typ = input_number.split()

    if typ[0] == "Счет":
        account_str = input_number

        return f"{account_str[:4]} **{account_str[-4:]}"
    else:
        account_str = input_number
        return f"{account_str[0:-16]} {account_str[-16:-12]} {account_str[-13:-10]}** **** {account_str[-4:]}"

def get_date (input_date: str) -> str:
    return f"{input_date[8:10]}.{input_date[5:7]}.{input_date[0:4]}"




