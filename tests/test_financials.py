from unittest.mock import mock_open, patch

import pytest

from src.read_csv import get_csv_data_dict
from src.read_xlsx import get_xlsx_data_dict
from tests.test_generators import test_info_csv, test_info_xlcx


def test_get_info_transaction(test_info_csv, test_info_xlcx):
    info_csv = list(get_csv_data_dict("../data/transactions.csv"))
    assert info_csv[0] == test_info_csv

    info_xlsx = list(get_xlsx_data_dict("../data/transactions_excel.xlsx"))
    assert info_xlsx[0] == test_info_xlcx


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_get_info_transactions_csv_xlsx(mock_file):
    assert open("../Data/test_transactions_csv.csv").read() == "data"
    mock_file.assert_called_with("../Data/test_transactions_csv.csv")

    assert open("../data/test_transactions_excel.xlsx").read() == "data"
    mock_file.assert_called_with("../data/test_transactions_excel.xlsx")
