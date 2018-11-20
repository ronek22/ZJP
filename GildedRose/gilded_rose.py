# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.increasing_items = {"Aged Brie", "Backstage passes to a TAFKAL80ETC concert"}
        self.legendary_items = {"Sulfuras, Hand of Ragnaros"}

    def decrease_quality(self, item):
        quality = 1 if item.sell_in >= 0 else 2
        if item.name == "Conjured Mana Cake":
            quality *= 2
            
        item.quality -= quality
        if item.quality < 0:
            item.quality = 0

    def increase_quality(self, item):
        quality = 1 if item.sell_in >= 0 else 2
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in <= 10:
                quality += 1
            if item.sell_in <= 5:
                quality += 1
            if item.sell_in < 0:
                item.quality = 0

        item.quality += quality
        if item.quality > 50:
            item.quality = 50

    def change_quality(self, item):
        if item.name in self.increasing_items:
            self.increase_quality(item)
        elif item.name not in self.legendary_items:
            self.decrease_quality(item)

    def update_quality(self):
        for item in self.items:
            item.sell_in -= 1
            self.change_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
