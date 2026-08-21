from typing import List

import pytest

from solution import contains_duplicate


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([1,2,3,1], True, id="one_duplicate"),
        pytest.param([1,2,3,4], False, id="no_duplicates"),
        pytest.param([1,1,1,3,3,4,3,2,4,2], True, id="multiple_duplicate"),
    ],
)
def test_contains_duplicate(nums: List[int], expected: bool) -> None:
    assert contains_duplicate(nums) == expected