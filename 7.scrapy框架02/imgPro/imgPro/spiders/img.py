# -*- coding: utf-8 -*-
import scrapy

from imgPro.items import ImgproItem
class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/']

    def parse(self, response):
        #解析图片地址和图片名称
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_src = 'http://www.521609.com'+li.xpath('./a[1]/img/@src').extract_first()
            img_name = li.xpath('./a[1]/img/@alt').extract_first()+'.jpg'

            item = ImgproItem()
            item['name'] = img_name
            item['src'] = img_src

            yield item
