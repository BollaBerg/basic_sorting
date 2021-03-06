import random
import pytest

# Import modules to test
from basic_sorting.selectionsort import selectionsort

def _create_list_of_integers(n):
    """Create a list of n integers."""
    list = []
    for _ in range(n):
        list.append(random.randint(0, 100))
    
    return list

def _create_list_of_floats(n):
    """Create a list of n floats."""
    list = []
    for _ in range(n):
        list.append(random.random() * 100)
    
    return list



class TestSelectionsortAscending:
    def test_selectionsort__on_integers(self):
        list = _create_list_of_integers(25)
        list_copy = list[:]
        assert selectionsort(list) == sorted(list_copy)

    def test_selectionsort__on_empty_list(self):
        assert selectionsort([]) == []

    def test_selectionsort__on_single_float(self):
        list = _create_list_of_floats(1)
        list_copy = list[:]
        assert selectionsort(list) == sorted(list_copy)

    def test_selectionsort__error(self):
        list = [1, 4, 5.77, 2, "a"]
        with pytest.raises(TypeError):
            selectionsort(list)



class TestSelectionsortDescending:
    def test_selectionsort__on_integers_descending(self):
        list = _create_list_of_integers(25)
        list_copy = list[:]
        assert selectionsort(list, descending=True) == sorted(list_copy, reverse=True)

    def test_selectionsort__on_empty_list_descending(self):
        assert selectionsort([], descending=True) == []

    def test_selectionsort__on_single_float_descending(self):
        list = _create_list_of_floats(1)
        list_copy = list[:]
        assert selectionsort(list, descending=True) == sorted(list_copy, reverse=True)

    def test_selectionsort__error_descending(self):
        list = [1, 4, 5.77, 2, "a"]
        with pytest.raises(TypeError):
            selectionsort(list, descending=True)



if __name__ == "__main__":
    pytest.main(["--verbose", __file__])