import pytest
from src.decorators import *


def test_successful_execution_console(capsys):

    @log()
    def add(a, b):
        return a + b

    result = add(3, 5)

    assert result == 8

    captured = capsys.readouterr()
    assert "add" in captured.out
    assert "результат: 8" in captured.out

def test_error_console(capsys):

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    output = captured.out + captured.err  # Проверяем оба потока

    assert "divide" in output
    assert "ZeroDivisionError" in output

