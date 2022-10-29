import pytest
from approvaltests.approvals import verify
from src.backstage_pass import BackstagePass

from src.gilded_rose import GildedRose
from src.item import Item
from src.gilded_item import GildedItem
from src.aged_brie import AgedBrie
from src.sulfuras import Sulfuras


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
            AgedBrie(name="Aged Brie", sell_in=2, quality=0),
        ]
    days = 5
    verify(gilded_rose_simulation(items, days))

def test_items_high_quality():
    items = [
            AgedBrie(name="Aged Brie", sell_in=10, quality=49),
            BackstagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=49),
            GildedItem(name="Item of Randomness", sell_in=10, quality=49)
        ]
    days = 3
    verify(gilded_rose_simulation(items, days))
    

def test_items_negative_sellin_high_quality():
    items = [
            AgedBrie(name="Aged Brie", sell_in=1, quality=49),
            BackstagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=49),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=49),
            GildedItem(name="Item of Randomness", sell_in=1, quality=49)
        ]
    days = 3
    verify(gilded_rose_simulation(items, days))

def test_adhoc_item_combos():
    items = [
             BackstagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=30),
             BackstagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=30),
             BackstagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=30),
             GildedItem(name="Item of Randomness", sell_in=1, quality=0),
             GildedItem(name="Item of Randomness", sell_in=1, quality=-1),
             GildedItem(name="An item of Randomness", sell_in=1, quality=-1),
             AgedBrie(name="Aged Brie", sell_in=-1, quality=51)
    ]
    days = 3
    verify(gilded_rose_simulation(items, days))