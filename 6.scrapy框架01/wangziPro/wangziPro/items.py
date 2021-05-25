# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WangziproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Filed()定义好的属性当做是一个万能类型的属性
    title = scrapy.Field()
    content = scrapy.Field()
