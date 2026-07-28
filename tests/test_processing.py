from src.processing import *


def test_filter_by_state(data_list, data_list_executed, data_list_canceled):
    assert filter_by_state(data_list) == data_list_executed
    assert filter_by_state(data_list, "EXECUTED") == data_list_executed
    assert filter_by_state([]) == []
    assert filter_by_state(data_list, "CANCELED") == data_list_canceled


def test_sort_by_date(data_list, data_filter, data_filter_reverse):
    assert sort_by_date(data_filter) == data_filter
    assert sort_by_date(data_filter, 1) == data_filter
    assert sort_by_date(data_filter, 0) == data_filter_reverse
    assert sort_by_date([]) == []
