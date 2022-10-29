# -*- coding: utf-8 -*-
from src.gilded_item import GildedItem
from src.aged_brie import AgedBrie
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item()


