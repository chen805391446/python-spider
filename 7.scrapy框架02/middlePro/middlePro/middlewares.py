# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals



class MiddleproDownloaderMiddleware(object):



    # 拦截所有(正常&异常)的请求
    #参数：request就是拦截到的请求，spider就是爬虫类实例化的对象
    def process_request(self, request, spider):
        print('process_request()')
        request.headers['User-Agent'] = 'xxx'
        # request.headers['Cookie'] = 'xxxxx'
        return None #or request
    #拦截所有的响应对象
    #参数：response拦截到的响应对象，request响应对象对应的请求对象
    def process_response(self, request, response, spider):
        print('process_response()')
        return response
    #拦截异常的请求
    #参数：request就是拦截到的发生异常的请求
    #作用：想要将异常的请求进行修正，将其变成正常的请求，然后对其进行重新发送
    def process_exception(self, request, exception, spider):
        #请求的ip被禁掉，该请求就会变成一个异常的请求
        request.meta['proxy'] = 'http://ip:port' #设置代理
        print('process_exception()')
        return request #将异常的请求修正后将其进行重新发送



