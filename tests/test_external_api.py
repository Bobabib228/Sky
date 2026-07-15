import os
from unittest import mock

import pytest

from src.external_api import currency_transfer

API_KEY = os.getenv("API_KEY")


@mock.patch("requests.request")
def test_currency_transfer(mock_request, operations):
    mock_response = mock.Mock()
    mock_response.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1784052125, "rate": 77.548},
        "date": "2026-07-14",
        "result": 637550.80076,
    }
    mock_request.return_value = mock_response
    func_res = currency_transfer(operations)
    assert func_res == 637550.80076
    mock_request.assert_called_once_with(
        "GET",
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37",
        headers={"apikey": API_KEY},
        data={},
    )
