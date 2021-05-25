# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from time import sleep
from scrapy.http import HtmlResponse#scrapy封装好的响应类

class WangyiproDownloaderMiddleware(object):


    def process_request(self, request, spider):

        return None
    #拦截所有的响应对象
    #整个工程发起的请求：1+5+n，相应也会有1+5+n个响应
    #只有指定的5个响应对象是不满足需求
    #直将不满足需求的5个指定的响应对象的响应数据进行篡改
    def process_response(self, request, response, spider):

        #将拦截到的所有的响应对象中指定的5个响应对象找出
        if request.url in spider.model_urls:
            bro = spider.bro
            #response表示的就是指定的不满足需求的5个响应对象
            #篡改响应数据：首先先获取满足需求的响应数据，将其篡改到响应对象中即可
            #满足需求的响应数据就可以使用selenium获取
            bro.get(request.url) #对五个板块的url发起请求
            sleep(2)
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            #捕获到了板块页面中加载出来的全部数据（包含了动态加载的数据）
            page_text = bro.page_source
            # response.text = page_text
            #返回了一个新的响应对象，新的对象替换原来不满足需求的旧的响应对象
            return HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request) # 5
        else:
            return response #1+n

    def process_exception(self, request, exception, spider):

        pass


