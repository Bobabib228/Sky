def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data: Список словарей, каждый из которых может содержать ключ 'state'.
        state: Значение, по которому производится фильтрация. По умолчанию 'EXECUTED'.

    Returns:
        Новый список словарей, у которых значение ключа 'state' равно заданному.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Сортирует список словарей по ключу 'date'.

    Args:
        data: Список словарей, каждый из которых должен содержать ключ 'date'.
        reverse: Порядок сортировки. True - убывание (по умолчанию), False - возрастание.

    Returns:
        Новый отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x.get('date', ''), reverse=reverse)

