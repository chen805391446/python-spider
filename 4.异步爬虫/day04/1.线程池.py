#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import time

from multiprocessing.dummy import Pool
urls = [
        'http://127.0.0.1:5000/bobo',
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/tom'
    ]
def get_request(url):
    page_text = requests.get(url=url).text
    return len(page_text)

#同步代码
# if __name__ == "__main__":
#     start = time.time()
#
#     for url in urls:
#         res = get_request(url)
#         print(res)
#     print('总耗时：',time.time()-start)
#异步代码
if __name__ == "__main__":
    start = time.time()
    pool = Pool(3) #3表示开启线程的数量
    #使用get_request作为回调函数，需要基于异步的形式对urls列表中的每一个列表元素进行操作
    #保证回调函数必须要有一个参数和返回值
    result_list = pool.map(get_request,urls)
    print(result_list)
    print('总耗时：', time.time() - start)
