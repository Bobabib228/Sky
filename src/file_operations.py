import csv

import openpyxl
import pandas as pd


def read_csv_transactions(file_path):
    """
    Читает транзакции из CSV файла.
    """
    try:
        df = pd.read_csv(file_path, encoding="utf-8-sig")
        if df.empty:
            return []
        return df.to_dict("records")
    except FileNotFoundError:
        raise
    except Exception:
        return []


def read_excel_transactions(file_path):
    """
    Читает транзакции из Excel файла.
    """
    try:
        df = pd.read_excel(file_path, index_col=0)
        if df.empty:
            return []
        return df.to_dict("records")
    except FileNotFoundError:
        raise
    except Exception as e:
        return e


def read_csv_transactions2(file_path):
    with open(file_path, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        data = [row for row in reader]
        return data
