import pytest
from approvaltests.approvals import verify

from src.gilded_rose import Item, GildedRose


def gilded_rose_simulation(items, days):
    result = ""
    for day in range(days):
        result += f"-------- day {day} -------- \n"
        result += "name, sellIn, quality \n"
        for item in items:
            result += str(item)
            result += "\n"
        result += "\n"
        GildedRose(items).update_quality()
    return result

def test_items():
    items = [
            Item(name="Aged Brie", sell_in=2, quality=0),
        ]
    days = 5
    verify(gilded_rose_simulation(items, days))

def test_items_high_quality():
    items = [
            Item(name="Aged Brie", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=49),
            Item(name="Item of Randomness", sell_in=10, quality=49)
        ]
    days = 3
    verify(gilded_rose_simulation(items, days))
    

def test_items_negative_sellin_high_quality():
    items = [
            Item(name="Aged Brie", sell_in=1, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=49),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=49),
            Item(name="Item of Randomness", sell_in=1, quality=49)
        ]
    days = 3
    verify(gilded_rose_simulation(items, days))

def test_adhoc_item_combos():
    items = [
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=30),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=30),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=30),
             Item(name="Item of Randomness", sell_in=1, quality=0),
             Item(name="Item of Randomness", sell_in=1, quality=-1),
             Item(name="An item of Randomness", sell_in=1, quality=-1),
             Item(name="Aged Brie", sell_in=-1, quality=51)
    ]
    days = 3
    verify(gilded_rose_simulation(items, days))