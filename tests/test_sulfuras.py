from src.sulfuras import Sulfuras

def test_sulfras_no_decrease_quality():
    sulfuras = Sulfuras('Sulfuras', sell_in=4, quality=5)

    sulfuras.update_item()

    assert sulfuras.quality == 5

def test_sulfras_no_decrease_quality_passed_sell_by():
    sulfuras = Sulfuras('Sulfuras', sell_in=-1, quality=5)

    sulfuras.update_item()

    assert sulfuras.quality == 5

def test_sulfuras_no_decrease_sell_by():
    sulfuras = Sulfuras('Sulfuras', sell_in=10, quality=5)

    sulfuras.update_item()

    assert sulfuras.sell_in == 10