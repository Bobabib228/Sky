import openpyxl
import pandas as pd



def read_csv_transactions(file_path):
    """
    Читает транзакции из CSV файла.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            return []
        return df.to_dict('records')
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
        return df.to_dict('records')
    except FileNotFoundError:
        raise
    except Exception as e:
        return e