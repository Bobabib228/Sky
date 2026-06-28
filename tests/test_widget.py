import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(number_MsCard, card, account_widget, account):
    assert mask_account_card(number_MsCard) == f"MasterCard {card}"
    assert mask_account_card(account_widget) == f"Счёт {account}"


@pytest.mark.parametrize(
    "value, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2025-06-17T02:26:18.671407", "17.06.2025")]
)
def test_get_date(value, expected):
    assert get_date(value) == expected
