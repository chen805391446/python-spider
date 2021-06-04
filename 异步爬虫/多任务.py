import asyncio
import requests
import time

# async def get_request(url):
#     print('正在请求的url: ',url)
#     time.sleep(2)                 # 出现了不支持异步模块的代码
#     print('请求结束',url)
#     return r'我通过t.result()返回'

async def get_request(url):
    print('正在请求的url：',url)
    await asyncio.sleep(2) # 支持异步模块的代码,要使用await关键字修饰，保证阻塞不会被跳过
    print('请求结束：',url)
    return 'bobo'

urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com'
]

def task_callback(t):
    print(t.result())

if __name__ == '__main__':
    start = time.time()
    # 建立一个任务列表
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    # 事件循环对象是用来注册所有的任务对象的，所以不能在循环中
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(tasks) 使用这种方法是错的
    # 不能把任务列表直接放在run_until_complete()函数内
    # 要使用wait方法对tasks进行封装才行
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时：', time.time() - start)

