from src.file_operations import read_csv_transactions, read_excel_transactions
from unittest.mock import patch, Mock
import pandas as pd


@patch('pandas.read_csv')
def test_read_csv_transactions(mock_read_csv, csv_data):
    mock_df = Mock()
    mock_df.empty = False
    mock_df.to_dict.return_value = csv_data
    mock_read_csv.return_value = mock_df


    result = read_csv_transactions('test.csv')


    assert result == csv_data
    mock_read_csv.assert_called_once_with('test.csv')
    mock_df.to_dict.assert_called_once_with('records')

@patch('pandas.read_excel')
def test_read_excel_transactions(mock_read_excel, csv_data):
    mock_df = Mock()
    mock_df.empty = False
    mock_df.to_dict.return_value = csv_data
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions('test.xlsx')

    assert result == csv_data
    mock_read_excel.assert_called_once_with('test.xlsx', index_col=0)
    mock_df.to_dict.assert_called_once_with('records')
