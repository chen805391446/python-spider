import asyncio
import requests
import time

# 构建一个特殊函数
async def get_request(url):
    print('正在请求的url: ',url)
    time.sleep(2)
    print('请求结束',url)
    return r'我通过t.result()返回'


# if __name__ == '__main__':
#     c = get_request('www.1.com')
#     # print(c)
# '''
# 在函数被async修饰后，会返回一个携程对象，此时函数内部的语句不会被立即执行
# <coroutine object get_request at 0x0000022A964FB9C0>
# sys:1: RuntimeWarning: coroutine 'get_request' was never awaited
# '''

# 参数t：就是该回调函数的调用者（任务对象）
def task_callback(t):
    print('I am a callback(),t= ',t)
    # result返回的就是特殊函数的返回值
    print('t.result()返回的是：',t.result())

if __name__ == '__main__':
    # c就是一个协程对象
    c = get_request('www.1.com')
    # 创建任务对象
    task = asyncio.ensure_future(c)
    # 给task绑定一个回调函数，该回调函数在任务对象进入事件循环后将不会再输出
    task.add_done_callback(task_callback)
    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 将任务对象注册到事件循环中，且开启事件循环
    loop.run_until_complete(task)

