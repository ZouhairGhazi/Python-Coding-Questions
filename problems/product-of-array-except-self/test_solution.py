from typing import List

import pytest

from solution import product_except_self


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([1,2,3,4], [24,12,8,6], id="basic_product"),
        pytest.param([-1,1,0,-3,3], [0,0,9,0,0], id="product_with_zero")
    ],
)
def test_max_profit(nums: List[int], expected: List[int]) -> None:
    assert product_except_self(nums) == expected