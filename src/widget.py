from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    result = ''
    if len(number.split()[-1]) == 16:
        mask_card = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{mask_card}"
    elif len(number.split()[-1]) == 20:
        mask_card = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{mask_card}"
    return result


state = input()
print(mask_account_card(state))


def get_new_data(data_new: str) -> str:
    data = datetime.strptime(data_new, "%Y-%m-%dT%H:%M:%S.%fZ")
    return data.strftime("%d.%m.%Y")


print(get_new_data(input()))
