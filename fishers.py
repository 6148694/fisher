#coding:utf-8
from app import create_app

app =create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=2030,threaded=True)
    #单进程、单线程
    #10个请求