import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_transfer(trans):
    amount = trans["operationAmount"]["amount"]
    currency = trans["operationAmount"]["currency"]["code"]
    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        payload = {}
        headers = {
            "apikey": API_KEY,
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        print(result)
        return float(result["result"])
    else:
        return float(amount)
