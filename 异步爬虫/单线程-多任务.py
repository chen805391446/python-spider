import requests
import asyncio
import time
import aiohttp
from lxml import etree
urls = [
    'http://localhost:5000/bobo',
    'http://localhost:5000/tom',
    'http://localhost:5000/jay'
]
# async def get_request(url):
#     # requests是一个不支持异步的模块,故加await没有用
#     page_text = await requests.get(url).text
#     return page_text

async def get_request(url):
    # 实例化好了一个请求对象
    async with aiohttp.ClientSession() as sess:
        # 调用get发起请求，返回一个响应对象
        # get/post(url,headers,params/data,proxy="http://ip:port")
        async with await sess.get(url=url) as response:
            # text()获取了字符串形式的响应数据
            # read()获取byte类型的响应数据
            page_text = await response.text()
            return page_text

# 对数据进行解析
# 解析函数的封装
def parse(t):
    # 获取请求到页面源码数据
    page_text = t.result()   # 这里的t表示特殊函数返回的page_text
    tree = etree.HTML(page_text)
    parse_text = tree.xpath('//a[@id="feng"]/text()')[0]
    print(parse_text)

if __name__ == "__main__":
    start = time.time()
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)  # 创建任务对象
        task.add_done_callback(parse)   # 创建回调函数对象，括号中参数用于数据解析
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时：',time.time()-start)