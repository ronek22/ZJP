import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item('foo', 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('foo', items[0].name)

    def test_in_date_foo_deterioration(self):
        items = [Item('foo', 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 9
        assert items[0].sell_in == 9

    def test_out_of_date_foo_deterioration(self):
        items = [Item('foo', -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 8
        assert items[0].sell_in == -2

    def test_quality_of_foo_never_becomes_negative(self):
        items = [Item('foo', 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 0
        assert items[0].sell_in == -1   

    def test_aged_brie_quality_increses_over_time_while_in_date(self):
        items = [Item('Aged Brie', 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 1
        assert items[0].sell_in == 9

    def test_aged_brie_quality_increses_by_two_when_out_of_date(self):
        items = [Item('Aged Brie', -5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 2
        assert items[0].sell_in == -6

    def test_aged_brie_quality_caps_at_50_when_out_of_date(self):
        items = [Item('Aged Brie', -5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 50
        assert items[0].sell_in == -6

    def test_aged_brie_quality_caps_at_50_when_in_date(self):
        items = [Item('Aged Brie', 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 50
        assert items[0].sell_in == 9

    def test_in_date_conjured_mana_cake_deterioration(self):
        items = [Item('Conjured Mana Cake', 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 8
        assert items[0].sell_in == 9

    def test_out_of_date_conjured_mana_cake_deterioration(self):
        items = [Item('Conjured Mana Cake', -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 6
        assert items[0].sell_in == -2

    def test_sulfuras_never_decreases_sell_by_or_quality(self):
        items = [Item('Sulfuras, Hand of Ragnaros', 100, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 30
        self.assertEquals(items[0].sell_in, 100)

    def test_sulfuras_can_be_over_fifty_in_quality(self):
        items = [Item('Sulfuras, Hand of Ragnaros', 100, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 80
        assert items[0].sell_in == 100

    def test_backstage_passes_while_ten_days_or_less_left(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 22
        assert items[0].sell_in == 9

    def test_backstage_passes_while_five_days_or_less_left(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 23
        assert items[0].sell_in == 4

    def test_backstage_passes_quality_after_sell_by(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 0)
        assert items[0].sell_in == -1


if __name__ == '__main__':
    unittest.main()