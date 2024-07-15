from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    result: str = ''
    if len(number.split()[-1]) == 16:
        mask_card = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{mask_card}"
    elif len(number.split()[-1]) == 20:
        mask_card = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{mask_card}"
    return result


state: str = input()
print(mask_account_card(state))
print(datetime.now().strftime('%d.%m.%Y'))
