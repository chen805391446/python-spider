# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from redis import Redis
class WangziproPipeline(object):

    fp = None
    #重写父类的两个方法
    def open_spider(self,spider):
        print('我是open_spider(),我只会在爬虫开始的时候执行一次！')
        self.fp = open('duanzi.txt','w',encoding='utf-8')
    def close_spider(self,spider):
        print('我是close_spider(),我只会在爬虫结束的时候执行一次！')
        self.fp.close()

    #该方法是用来接收item对象。一次只能接收一个item，说明该方法会被调用多次
    #参数item：就是接收到的item对象
    def process_item(self, item, spider):
        # print(item) #item其实就是一个字典
        self.fp.write(item['title']+':'+item['content']+'\n')
        #将item存储到本文文件
        return item

#将数据存储到mysql中
class MysqlPileLine(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',db='spider',charset='utf8')
        print(self.conn)
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()
        sql = 'insert into duanziwang values ("%s","%s")'%(item['title'],item['content'])

        #事物处理
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

#将数据写入redis
class RedisPileLine(object):
    conn = None
    def open_spider(self,spider):
        self.conn = Redis(host='127.0.0.1',port=6379)
        print(self.conn)
    def process_item(self,item,spider):
        #报错：将redis模块的版本指定成2.10.6即可。pip install -U redis==2.10.6
        self.conn.lpush('duanziData',item)
