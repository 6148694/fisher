#coding:utf-8
from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    #9787501524044
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'
    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        #dict
        return result
    @classmethod
    def search_by_keyword(cls,keyword,page=1):
        url = cls.keyword_url.format(keyword,current_app.config['PER_PAGE'],cls.calculate_start(page))
        #配置里读取文件   这里没有APP核心对象  所以要用current_app   类似代理
        result = HTTP.get(url)
        return result
    @staticmethod
    def calculate_start(page):
        return (page-1)* current_app.config['PER_PAGE']