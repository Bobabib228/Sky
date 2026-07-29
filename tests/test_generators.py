from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(data_card_transaction, data_card_transaction_canceled):
    generetor = filter_by_currency(data_card_transaction, "USD")
    assert next(generetor) == data_card_transaction_canceled


def test_transaction_descriptions(data_card_transaction, transaction_descriptions_canceled):
    generetor = transaction_descriptions(data_card_transaction)
    assert next(generetor) == transaction_descriptions_canceled


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
