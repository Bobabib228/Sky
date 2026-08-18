import re


def process_bank_search(data:list[dict], search:str)->list[dict]:
    result = []
    for item in data:
        if re.search(search, item.get('description'), re.IGNORECASE):
            result.append(item)
    return result


def process_bank_operations(data:list[dict], categories:list)->dict:
    result = {}
    for category in categories:
      counter = 0
      for item in data:
        if re.search(category, item.get('description'), re.IGNORECASE):
            counter += 1
      result[category] = counter
    return result
