# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#该默认管道无法帮助我们请求图片数据，因此该管道我们就不用
# class ImgproPipeline(object):
#     def process_item(self, item, spider):
#         return item

#管道需要接受item中的图片地址和名称，然后再管道中请求到图片的数据对其进行持久化存储
from scrapy.pipelines.images import ImagesPipeline #提供了数据下载功能
from scrapy.pipelines.media import MediaPipeline
from scrapy.pipelines.files import FilesPipeline
import scrapy
class ImgsPipiLine(ImagesPipeline):
    #根据图片地址发起请求
    def get_media_requests(self, item, info):
        # print(item)
        yield scrapy.Request(url=item['src'],meta={'item':item})
    #返回图片名称即可
    def file_path(self, request, response=None, info=None):
        #通过request获取meta
        item = request.meta['item']
        filePath = item['name']
        return filePath #只需要返回图片名称
    #将item传递给下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item