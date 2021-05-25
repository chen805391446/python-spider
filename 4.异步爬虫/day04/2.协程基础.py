#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import asyncio
import requests
import time

async def get_request(url):
    print('正在请求的url：',url)
    time.sleep(2)
    print('请求结束：',url)
    return 'bobo'

#回调函数的封装
#参数t：就是该回调函数的调用者（任务对象）
def task_callback(t):
    print('i am task_callback(),参数t：',t)
    #result返回的就是特殊函数的返回值
    print('t.result()返回的是：',t.result())

if __name__ == "__main__":
    #c就是一个协程对象
    c = get_request('www.1.com')

    #任务对象就是对协程对象的进一步封装
    task = asyncio.ensure_future(c)
    #给task绑定一个回调函数
    task.add_done_callback(task_callback)
    #创建事件循环对象
    loop = asyncio.get_event_loop()
    #将任务对象注册到事件循环中且开启事件循环
    loop.run_until_complete(task)