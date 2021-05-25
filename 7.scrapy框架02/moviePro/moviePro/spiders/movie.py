# -*- coding: utf-8 -*-
import scrapy
from moviePro.items import MovieproItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567kan.com/index.php/vod/show/id/5.html']
    url = 'https://www.4567kan.com/index.php/vod/show/id/5/page/%d.html'
    pageNum = 2
    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div/a/@title').extract_first()
            detail_url = 'https://www.4567kan.com'+li.xpath('./div/a/@href').extract_first()

            item = MovieproItem()
            item['title'] = title

            #对详情页url发起请求
            #meta作用：可以将meta字典传递给callback
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})

        if self.pageNum < 5:
            new_url = format(self.url%self.pageNum)
            self.pageNum += 1
            yield scrapy.Request(url=new_url,callback=self.parse)

    #被用作于解析详情页的数据
    def parse_detail(self,response):
        #接受传递过来的meta
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]').extract_first()
        item['desc'] = desc

        yield item