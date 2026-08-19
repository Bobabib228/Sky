import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s:  %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по правилу XXXX XX** **** XXXX, принимает на вход строковые значения
    """
    logger.info("Starting get_mask_card_number")
    card_str = card_number
    if len(card_str) > 16:
        logger.error("Номер карты введен некорректно")
        return "Номер карты введен некорректно"
    elif card_str == "0":
        logger.error("Номер карты введен некорректно")
        return "Номер карты введен некорректно"
    else:
        logger.info("Ending get_mask_card_number")
        return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета по правилу **XXXX, принимает на вход строковые значения
    """
    logger.info("Starting get_mask_account")
    account_str = account_number
    logger.info("Ending get_mask_account")
    return f"**{account_str[-4:]}"