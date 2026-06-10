import pytest

@pytest.fixture
def card():
    return "1234 56** **** 4567"

@pytest.fixture
def account():
    return "**7890"

@pytest.fixture
def number_MsCard():
    return "MasterCard 1234567891234567"

@pytest.fixture
def account_widget():
    return "Счёт 12345678901234567890"