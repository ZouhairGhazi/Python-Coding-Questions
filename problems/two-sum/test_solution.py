from typing import List

import pytest

from solution import two_sum


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        pytest.param([2, 7, 11, 15], 9, [0, 1], id="basic_pair"),
        pytest.param([3, 2, 4], 6, [1, 2], id="pair_not_at_start"),
        pytest.param([3, 3], 6, [0, 1], id="duplicate_values_pair"),
        pytest.param([3, 2, 4], 8, [-1], id="no_pair_found"),
    ],
)
def test_two_sum(nums: List[int], target: int, expected: List[int]) -> None:
    assert two_sum(nums, target) == expected
