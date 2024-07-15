import pytest
from src.processing import filter_by_state, sort_by_date, list_of_dicts


@pytest.fixture
def test_initial_list():
    return 'EXECUTED'


@pytest.fixture
def test_initial_list_1():
    return list_of_dicts
