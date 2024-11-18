import pytest
import inspect
from assignment import rotate_matrix_90_clockwise, search_in_matrix

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[5, 1], [3, 7]], [[3, 5], [7, 1]]),
    ([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]], 
     [[130, 90, 50, 10], [140, 100, 60, 20], [150, 110, 70, 30], [160, 120, 80, 40]])
])
def test1(matrix, expected):
    assert rotate_matrix_90_clockwise(matrix) == expected
    assert check_contains_loop(rotate_matrix_90_clockwise)

@pytest.mark.parametrize("matrix, target, expected", [
    ([[3, 8, 2], [5, 10, 7], [6, 1, 9]], 10, [1, 1]),
    ([[4, 0, 1], [9, 2, 3], [5, 6, 7]], 6, [2, 1]),
    ([[3, 5], [7, 1]], 8, [])
])
def test2(matrix, target, expected):
    assert search_in_matrix(matrix, target) == expected
    assert check_contains_loop(search_in_matrix)
