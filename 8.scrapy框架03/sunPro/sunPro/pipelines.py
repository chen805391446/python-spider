# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SunproPipeline(object):
    def process_item(self, item, spider):
        # if item.__class__.__name__ == 'SunproItem':
        #     title = item['title']
        #     status = item['status']
        #     print(title+':'+status)
        # else:
        #     content = item['content']
        #     print(content)
        print(item)
        return item
