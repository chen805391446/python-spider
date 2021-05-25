#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  time
import requests
import asyncio
import asyncio

# async def get_request(url):
#     print('正在请求的url：',url)
#     time.sleep(2) #出现了不支持异步模块的代码
#     print('请求结束：',url)
#     return 'bobo'

async def get_request(url):
    print('正在请求的url：',url)
    await asyncio.sleep(2) #支持异步模块的代码
    print('请求结束：',url)
    return 'bobo'

urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com'
]
if __name__ == "__main__":
    start = time.time()
    tasks = [] #多任务列表
    #1.创建协程对象
    for url in urls:
        c = get_request(url)
        #2.创建任务对象
        task = asyncio.ensure_future(c)
        tasks.append(task)

    #3.创建事件循环对象
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(tasks)
    #必须使用wait方法对tasks进行封装才可
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时：',time.time()-start)

#问题：
    #- wait方法是干嘛的
    #- 说好的异步效果呢