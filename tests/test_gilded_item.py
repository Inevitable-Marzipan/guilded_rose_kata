from src.gilded_item import GildedItem

def test_gilded_item_one_day():
    gilded_item = GildedItem("item", sell_in=1, quality=10)

    gilded_item.update_item()

    assert gilded_item.quality == 9
    assert gilded_item.sell_in == 0

def test_gilded_item_sell_by_passed_one():
    gilded_item = GildedItem("item", sell_in=-1, quality=4)

    gilded_item.update_item()

    assert gilded_item.quality == 2

def test_gilded_item_sell_by_passed_two():
    gilded_item = GildedItem("item", sell_in=0, quality=4)

    gilded_item.update_item()

    assert gilded_item.quality == 2

def test_gilded_item_quality_non_negative():
    gilded_item = GildedItem("item", sell_in=4, quality=0)

    gilded_item.update_item()

    assert gilded_item.quality == 0
