# -*- coding: utf-8 -*-
"""
Create Time: 2021/6/22 12:45 下午
Author: Aries
"""
from flask import Flask,current_app,Request
app =Flask(__name__)

#a = current_app
#d = current_app.config['DEBUG']

# ctx =app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']

#实现了上下文协议的对象使用with
#上下文管理器

import threading

def worker():
    print("i am  wanglei")
    t = threading.current_thread()
    print(t.getName())

t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker,name='王磊的线程')
new_t.start()
