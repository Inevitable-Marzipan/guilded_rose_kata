from src.aged_brie import AgedBrie

def test_aged_brie_quality_increase():
    aged_brie = AgedBrie("Aged Brie", sell_in=3, quality=5)

    aged_brie.update_item()

    assert aged_brie.quality == 6

def test_aged_brie_quality_increase_passed_sell_by():
    aged_brie = AgedBrie("Aged Brie", sell_in=-1, quality=5)

    aged_brie.update_item()

    assert aged_brie.quality == 7