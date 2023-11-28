import pytest
from integer_list import IntegerList

@pytest.fixture
def integer_list():
    return IntegerList()

# Test pour la méthode add_integer(num)
@pytest.mark.parametrize("input_nums, expected_result", [
    ([1, 2, 3], [1, 2, 3]),
    ([], [5]),
    ([10, 20, 30], [10, 20, 30, 40]),
    ([5, 5, 5], [5, 5, 5, 5]),
])
def test_add_integer(integer_list, input_nums, expected_result):
    for num in input_nums:
        integer_list.add_integer(num)
    assert integer_list.numbers == expected_result

# Test pour la méthode remove_integer(num)
@pytest.mark.parametrize("initial_nums, num_to_remove, expected_result", [
    ([1, 2, 3], 2, [1, 3]),
    ([], 5, []),
    ([10, 20, 30], 30, [10, 20]),
    ([5, 5, 5], 5, [5, 5]),
])
def test_remove_integer(integer_list, initial_nums, num_to_remove, expected_result):
    integer_list.numbers = initial_nums
    integer_list.remove_integer(num_to_remove)
    assert integer_list.numbers == expected_result

# Test pour la méthode get_average()
@pytest.mark.parametrize("input_nums, expected_average", [
    ([1, 2, 3], 2),
    ([], pytest.raises(ValueError)),
    ([10, 20, 30], 20),
    ([5, 5, 5], 5),
])
def test_get_average(integer_list, input_nums, expected_average):
    for num in input_nums:
        integer_list.add_integer(num)
    
    if expected_average == pytest.raises(ValueError):
        with expected_average:
            integer_list.get_average()
    else:
        assert integer_list.get_average() == expected_average

# Test pour la méthode get_max()
@pytest.mark.parametrize("input_nums, expected_max", [
    ([1, 2, 3], 3),
    ([], pytest.raises(ValueError)),
    ([10, 20, 30], 30),
    ([5, 5, 5], 5),
])
def test_get_max(integer_list, input_nums, expected_max):
    for num in input_nums:
        integer_list.add_integer(num)
    
    if expected_max == pytest.raises(ValueError):
        with expected_max:
            integer_list.get_max()
    else:
        assert integer_list.get_max() == expected_max

# Test pour la méthode get_min()
@pytest.mark.parametrize("input_nums, expected_min", [
    ([1, 2, 3], 1),
    ([], pytest.raises(ValueError)),
    ([10, 20, 30], 10),
    ([5, 5, 5], 5),
])
def test_get_min(integer_list, input_nums, expected_min):
    for num in input_nums:
        integer_list.add_integer(num)
    
    if expected_min == pytest.raises(ValueError):
        with expected_min:
            integer_list.get_min()
    else:
        assert integer_list.get_min() == expected_min
