# 通过render_template这个类可以返回模板目录中的静态文件
from flask import Flask,render_template
from time import sleep
# 1，实例化一个app对象
app = Flask(__name__)

#创建视图函数&路由地址
@app.route('/bobo') # 执行函数后会得到一个IP地址+端口号，点击进去加上/bobo就会访问到text.html
def index_1():
    sleep(2)
    return render_template('test.html')

@app.route('/jay')
def index_2():
    sleep(2)
    return render_template('test.html')

@app.route('/tom')
def index_3():
    sleep(2)
    return render_template('test.html')

if __name__ == "__main__":
    #debug=True表示开启调试模式：服务器端代码被修改后按下保存键会自动重启服务
    app.run(debug=True)