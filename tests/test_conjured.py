from statistics import quantiles
from src.conjured import Conjured

def test_conjured_degrade_twice_as_fast():
    item = Conjured("conjured", sell_in=1, quality=10)

    item.update_item()

    assert item.quality == 8