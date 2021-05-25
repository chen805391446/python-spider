# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    status = scrapy.Field()
    content = scrapy.Field()

class SunProItemDetail(scrapy.Item):
    content = scrapy.Field()
