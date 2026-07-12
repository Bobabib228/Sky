import json

def load_transactions(file_path):
    """
    Загружает транзакции из JSON-файла.
    Возвращает пустой список, если файл не найден, пустой или содержит не список.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError, AttributeError):
        return []










