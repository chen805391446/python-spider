# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件名称：当前源文件的唯一标识
    name = 'first'
    #允许的域名
    #allowed_domains = ['www.baidu.com']

    #起始的url列表：只可以存储url
    #作用：列表中存储的url都会被进行get请求的发送
    start_urls = ['https://www.baidu.com/','https://www.sogou.com']

    #数据解析
    #parse方法调用的次数完全取决于请求的次数
    #参数response：表示的就是服务器返回的响应对象
    def parse(self, response):
        print(response)
