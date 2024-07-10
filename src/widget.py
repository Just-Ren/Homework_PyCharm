from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """ Формула принимает импортированные маски и переводит вводимые клиентом данные
    в описаную в masks.py форму"""
    result: str = ''
    if len(number.split()[-1]) == 16:
        mask_card = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{mask_card}"
    elif len(number.split()[-1]) == 20:
        mask_card = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{mask_card}"
    return result


def get_data(input_string: str) -> str | None:
    date = input_string.split("T")[0]
    formatted_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    return formatted_date


state: str = input()
print(mask_account_card(state))

calendar: str = input()
print(get_data(calendar))
