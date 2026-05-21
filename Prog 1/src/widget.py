def mask_account_card(input_number: str) -> str:

    typ = input_number.split()

    if typ[0] == "Счет":
        account_str = input_number

        return f"{account_str[:4]} **{account_str[-4:]}"
    else:
        account_str = input_number
        return f"{account_str[0:-16]} {account_str[-16:-12]} {account_str[-13:-10]}** **** {account_str[-4:]}"

print (mask_account_card("Maestro 7000792289606361"))


