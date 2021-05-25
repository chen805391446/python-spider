USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

# 今日内容:
- CrawlSpider深度爬取
- selenium在scrapy中的使用
- 分布式
- 增量式


## CrawlSpider实现的深度爬取
    - 通用方式：CrawlSpider+Spider实现

## selenium在scrapy中的使用
    - https://news.163.com/
    - 爬取网易新闻中的国内，国际，军事，航空，无人机这五个板块下所有的新闻数据（标题+内容）
- 分析
    - 首页没有动态加载的数据
        - 爬取五个板块对应的url
    - 每一个板块对应的页面中的新闻标题是动态加载
        - 爬取新闻标题+详情页的url（***）
    - 每一条新闻详情页面中的数据不是动态加载
        - 爬取的新闻内容

- selenium在scrapy中的使用流程
    - 1.在爬虫类中实例化一个浏览器对象，将其作为爬虫类的一个属性
    - 2.在中间件中实现浏览器自动化相关的操作
    - 3.在爬虫类中重写closed(self,spider),在其内部关闭浏览器对象


## 分布式
- 实现方式：scrapy+redis（scrapy结合着scrapy-redis组件）
- 原生的scrapy框架是无法实现分布式
    - 什么是是分布式
        - 需要搭建一个分布式的机群，让后让机群中的每一台电脑执行同一组程序，让其对同一组资源
            进行联合且分布的数据爬取。
    - 为什么原生的scrapy框架无法实现分布式？
        - 调度器无法被分布式机群共享
        - 管道无法分布式机群被共享
    - 如何实现分布式：使用scrapy-redis组件即可
    - scrapy-redis组件的作用：
        - 可以给原生的scrapy框架提供共享的管道和调度器
        - pip install scrapy-redis
- 实现流程
    1.修改爬虫文件
        - 1.1 导包：from scrapy_redis.spiders import RedisCrawlSpider
        - 1.2 修改当前爬虫类的父类为：RedisCrawlSpider
        - 1.3 将start_url替换成redis_keys的属性，属性值为任意字符串
            - redis_key = 'xxx'：表示的是可以被共享的调度器队列的名称，最终是需要将起始的url手动
            放置到redis_key表示的队列中
        - 1.4 将数据解析的补充完整即可
    2.对settings.py进行配置
        - 指定调度器
            # 增加了一个去重容器类的配置, 作用使用Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
            DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
            # 使用scrapy-redis组件自己的调度器
            SCHEDULER = "scrapy_redis.scheduler.Scheduler"
            # 配置调度器是否要持久化, 也就是当爬虫结束了, 要不要清空Redis中请求队列和去重指纹的set。如果是True, 就表示要持久化存储, 就不清空数据, 否则清空数据
            SCHEDULER_PERSIST = True
        - 指定管道
            ITEM_PIPELINES = {
                'scrapy_redis.pipelines.RedisPipeline': 400
            }
            - 特点：该种管道只可以将item写入redis
        - 指定redis
            REDIS_HOST = 'redis服务的ip地址'
            REDIS_PORT = 6379
    3.配置redis的配置文件（redis.window.conf）
        - 解除默认绑定
            - 56行：#bind 127.0.0.1
        - 关闭保护模式
            - 75行：protected-mode no
     4.启动redis服务和客户端
     5.执行scrapy工程（不要在配置文件中加入LOG_LEVEL）
        - 程序会停留在listening位置：等待起始的url加入
     6.向redis_key表示的队列中添加起始url
        - 需要在redis的客户端执行如下指令：（调度器队列是存在于redis中）
            - lpush sunQueue http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1




## 增量式
- 概念：监测网站数据更新的情况，以便于爬取到最新更新出来的数据。
- 实现核心：去重
- 实战中去重的方式：记录表
    - 记录表需要记录什么？记录的一定是爬取过的相关信息。
        - 爬取过的相关信息：每一部电影详情页的url
        - 只需要使用某一组数据，该组数据如果可以作为该部电影的唯一标识即可，刚好电影详情页的url
          就可以作为电影的唯一标识。只要可以表示电影唯一标识的数据我们统称为数据指纹。
- 去重的方式对应的记录表：
    - python中的set集合（不可以）
        - set集合无法持久化存储
    - redis中的set可以的
        - 可以持久化存储

- 数据指纹一般是经过加密
    - 当前案例的数据指纹没有必要加密。
    - 什么情况数据指纹需要加密？
        - 如果数据的唯一标识标识的内容数据量比较大，可以使用hash将数据加密成32位的密文。
            - 目的是为了节省空间。




