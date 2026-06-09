import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():

    with pytest.raises(TypeError):
        get_mask_card_number(1234567891234567)

    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"
    assert get_mask_card_number("12345678912345678") == "Номер карты введен некорректно"
    assert get_mask_card_number("0") == "Номер карты введен некорректно"



def test_get_mask_account():

    with pytest.raises(TypeError):
        get_mask_account(123456)

    assert get_mask_account("123456") == "**3456"
    assert get_mask_account("12345678912345678") == "Номер счёта введен некорректно"
    assert get_mask_account("0") == "Номер счёта введен некорректно"





