import pytest

def convert_to_eur(amounts, rates):
    return [amount * rate for amount, rate in zip(amounts, rates)]

def test_convert_to_eur():
    amounts = [100, 200, 300]
    rates = [1.2, 0.8, 1.5]
    expected_result = [120.0, 160.0, 450.0]
    assert convert_to_eur(amounts, rates) == expected_result

def test_convert_to_eur_empty_lists():
    amounts = []
    rates = []
    expected_result = []
    assert convert_to_eur(amounts, rates) == expected_result

def test_convert_to_eur_different_length_lists():
    amounts = [100, 200, 300]
    rates = [1.2, 0.8]
    with pytest.raises(ValueError):
        convert_to_eur(amounts, rates)

def test_convert_to_eur_non_numeric_values():
    amounts = [100, '200', 300]
    rates = [1.2, 0.8, 1.5]
    with pytest.raises(TypeError):
        convert_to_eur(amounts, rates)
