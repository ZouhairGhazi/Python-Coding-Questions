from typing import List

import pytest

from solution import max_sub_array


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([1, 2, 3, 1, 10, 5], 22, id="all_positive_ints"),
        pytest.param([2, 3, -1], 5, id="one_negative"),
        pytest.param([-2,1,-3,4], 4, id="multiple_negatives"),
        pytest.param([-2,1,-3,4,-1,2,1,-5,4], 6, id="multiple_negatives_2")
    ],
)
def test_contains_duplicate(nums: List[int], expected: int) -> None:
    assert max_sub_array(nums) == expected