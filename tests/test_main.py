# test_calculator.py
import pytest
from calculator import calculate_average

def test_calculate_average_empty_list():
    assert calculate_average([]) == 0

def test_calculate_average_single_element():
    assert calculate_average([5]) == 5

def test_calculate_average_even_number_of_elements():
    assert calculate_average([1, 2, 3, 4]) == 2.5

def test_calculate_average_odd_number_of_elements():
    assert calculate_average([1, 2, 3, 4, 5]) == 3

def test_calculate_average_with_negative_numbers():
    assert calculate_average([-1, 0, 1]) == 0

def test_calculate_average_with_floats():
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5
