# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoldenGlobesNomineesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    award_name = scrapy.Field()
    nominee_1 = scrapy.Field()
    nominee_2 = scrapy.Field()
    nominee_3 = scrapy.Field()
    nominee_4 = scrapy.Field()
    nominee_5 = scrapy.Field()

class GoldenGlobesPresenters(scrapy.Item):
	presenter = scrapy.Field()