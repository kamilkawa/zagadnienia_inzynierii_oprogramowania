import pytest

from calculator import Calculator


def test_sum_returns_expected_value():
    calculator = Calculator(9, 3)
    assert calculator.sum() == pytest.approx(12.0)


def test_subtract_returns_expected_value():
    calculator = Calculator(9, 3)
    assert calculator.subtract() == pytest.approx(6.0)


def test_multiply_returns_expected_value():
    calculator = Calculator(9, 3)
    assert calculator.multiply() == pytest.approx(27.0)


def test_divide_returns_expected_value():
    calculator = Calculator(9, 3)
    assert calculator.divide() == pytest.approx(3.0)


def test_divide_by_zero_returns_none_and_prints_message(capsys):
    calculator = Calculator(5, 0)

    result = calculator.divide()
    captured = capsys.readouterr()

    assert result is None
    assert "Błąd: dzielenie przez zero, operacja nie została wykonana." in captured.out


def test_divide_zero_by_zero_returns_none_and_prints_message(capsys):
    calculator = Calculator(0, 0)

    result = calculator.divide()
    captured = capsys.readouterr()

    assert result is None
    assert "Błąd: dzielenie przez zero, operacja nie została wykonana." in captured.out


def test_numeric_strings_are_converted():
    calculator = Calculator("10", "2")
    assert calculator.divide() == pytest.approx(5.0)


def test_invalid_first_operand_raises_value_error():
    with pytest.raises(ValueError) as error:
        Calculator("string_value", 3)

    assert "Argument op1 musi być liczbą." in str(error.value)


def test_invalid_second_operand_raises_value_error():
    with pytest.raises(ValueError) as error:
        Calculator(3, object())

    assert "Argument op2 musi być liczbą." in str(error.value)
