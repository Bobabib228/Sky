def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по правилу XXXX XX** **** XXXX, принимает на вход строковые значения
    """

    card_str = card_number

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета по правилу **XXXX, принимает на вход строковые значения
    """

    account_str = account_number

    return f"**{account_str[-4:]}"
