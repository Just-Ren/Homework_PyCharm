from typing import Any

list_of_dicts = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_of_dict: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """
    Функция принимает на вход список словарей и значение для ключа и возвращает новый
    список содержащий только те словари у которых ключ содержит переданное в функцию
    значение.
    """
    return [data_dict for data_dict in list_of_dict if data_dict.get("state") == state]


def sort_by_date(date_list: list, reverse_list: bool = True) -> list | bool:
    """Return filtered list by date"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list
