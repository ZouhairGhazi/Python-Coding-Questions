from typing import List

import pytest

from solution import max_profit


@pytest.mark.parametrize(
    ("prices", "expected"),
    [
        pytest.param([7, 1, 5, 3, 6, 4], 5, id="profit_after_dip"),
        pytest.param([7, 6, 4, 3, 1], 0, id="prices_only_decrease"),
        pytest.param([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9], 9, id="multiple_dips_and_peaks"),
    ],
)
def test_max_profit(prices: List[int], expected: int) -> None:
    assert max_profit(prices) == expected