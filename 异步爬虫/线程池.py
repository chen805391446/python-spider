from multiprocessing.dummy import Pool
import requests
import time

urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
    ]
def get_request(url):
    page_text = requests.get(url=url).text
    return len(page_text)       # 如果有信息，则表示请求成功

# 同步代码
# if __name__ == "__main__":
#     start = time.time()
#
#     for url in urls:
#         res = get_request(url)
#         print(res)
#     print('总耗时：',time.time()-start)

# 总耗时： 6.560534477233887 并没有实现快速爬取

#异步代码
if __name__ == "__main__":
    start = time.time()
    pool = Pool(3) # 3表示开启线程的数量
    # 使用get_request作为回调函数，需要基于异步的形式对urls列表中的每一个列表元素进行操作
    # 保证回调函数必须要有一个参数和返回值
    # 该回调函数的参数就是从列表中得到的每个url值
    # 多需要传递多个参数，则将多个参数封装成一个字典然后传给回调函数
    # 由于map需要接收一个返回值，故还必须要一个返回值，map后的值又会有一个值来接收，这里是result_list
    # map返回的是一个列表
    result_list = pool.map(get_request,urls)
    print(result_list)                          # [1001, 1001, 1001]
    print('总耗时：', time.time() - start)

# 总耗时： 2.5880157947540283 时间相对于上一个缩减了三倍