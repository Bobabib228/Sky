import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card):

    with pytest.raises(TypeError):
        get_mask_card_number(1234567891234567)

    assert get_mask_card_number("1234567891234567") == card
    assert get_mask_card_number("12345678912345678") == "Номер карты введен некорректно"
    assert get_mask_card_number("0") == "Номер карты введен некорректно"


def test_get_mask_account(account):

    with pytest.raises(TypeError):
        get_mask_account(123456)

    assert get_mask_account("12345678910234567890") == account
    assert get_mask_account("12345678912345678") == "Номер счёта введен некорректно"
    assert get_mask_account("0") == "Номер счёта введен некорректно"
