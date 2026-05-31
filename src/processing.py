def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data: Список словарей, каждый из которых может содержать ключ 'state'.
        state: Значение, по которому производится фильтрация. По умолчанию 'EXECUTED'.

    Returns:
        Новый список словарей, у которых значение ключа 'state' равно заданному.
    """
    return [item for item in data if item.get('state') == state]