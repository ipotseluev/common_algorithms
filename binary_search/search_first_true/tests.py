from algo_complicated import MyComplicateAlgorithm
from algo_lo_hi import AlgoLoHi

import pytest


test_cases = [
    # 3
    ([False, False, False], -1),
    ([True, False, False], 0),
    ([True, True, False], 1),
    ([True, True, True], 2),
    # 4
    ([False, False, False, False], -1),
    ([True, False, False, False], 0),
    ([True, True, False, False], 1),
    ([True, True, True, False], 2),
    ([True, True, True, True], 3),
    # 5
    ([False, False, False, False, False], -1),
    ([True, False, False, False, False], 0),
    ([True, True, False, False, False], 1),
    ([True, True, True, False, False], 2),
    ([True, True, True, True, False], 3),
    ([True, True, True, True, True], 4),
    # 6
    ([False, False, False, False, False, False], -1),
    ([True, False, False, False, False, False], 0),
    ([True, True, False, False, False, False], 1),
    ([True, True, True, False, False, False], 2),
    ([True, True, True, True, False, False], 3),
    ([True, True, True, True, True, False], 4),
    ([True, True, True, True, True, True], 5),
]


@pytest.mark.parametrize(
    argnames='array, expected_index',
    argvalues=test_cases

)
def test_my_bad_algo(array, expected_index):
    obj = MyComplicateAlgorithm()
    assert obj.search_last_true(array=array) == expected_index


@pytest.mark.parametrize(
    argnames='array, expected_index',
    argvalues=test_cases

)
def test_algo_lo_hi(array, expected_index):
    obj = AlgoLoHi()
    assert obj.search_last_true(array=array) == expected_index
