def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по правилу XXXX XX** **** XXXX, принимает на вход строковые значения
    """

    card_str = card_number
    if len(card_str) > 16:
        return "Номер карты введен некорректно"
    elif card_str == "0":
        return "Номер карты введен некорректно"
    else:
        return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета по правилу **XXXX, принимает на вход строковые значения
    """

    account_str = account_number
    if len(account_str) == 20:
        return f"**{account_str[-4:]}"
    else:
        return "Номер счёта введен некорректно"