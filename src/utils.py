import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path):
    """
    Загружает транзакции из JSON-файла.
    Возвращает пустой список, если файл не найден, пустой или содержит не список.
    """
    logger.info("Starting load_transactions")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Ending load_transactions")
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError, AttributeError) as e:
        logger.error(e)
        return []
