# -*- coding: utf-8 -*-
import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https1://www.baidu123.com/','https://www.sogou.com']

    def parse(self, response):
        print(response)
